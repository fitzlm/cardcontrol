import { Component, OnInit } from '@angular/core';
import {Router, ActivatedRoute} from "@angular/router";
import {UserService} from "../shared/user.service";

@Component({
  selector: 'app-user-home',
  templateUrl: './user-home.component.html',
  styleUrls: ['./user-home.component.scss']
})
export class UserHomeComponent implements OnInit {

  activeLinkIndex = 0;

  navLinks = [
    {route: '', label: 'My ID'},
    {route: '/areas', label: 'My Areas'},
    {route: '/request', label: 'Request Access'}
  ];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private userService: UserService
  ) {

    function findTab(nav) {
      if (nav.route === '') {
        return router.url === '' || router.url === '/';
      }
      return router.url.indexOf(nav.route) !== -1;
    }

    this.activeLinkIndex =
      this.navLinks.indexOf(this.navLinks.find(findTab));
  }

  ngOnInit() {
    this.userService.userAccount.filter(data => data !== null).subscribe(
      data => {
        this.isAdmin = data.manager_level > 0
      }
    )
  }

  get utln () {
    return this.userService.getUtln();
  }

  isAdmin : boolean = false;

  settings() {
    this.activeLinkIndex = -1;
    this.router.navigate(['account']);
  }

  logOut() {
    // alert("Logging out");
  }

}

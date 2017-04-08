#!/bin/bash
set -e
node --max_old_space_size=2000 ./node_modules/.bin/ng build --prod --verbose --output-path /home/ec2-user/cardcontrol/dist/

sudo rm -r /dist/
sudo mv /home/ec2-user/cardcontrol/dist/ /dist
#!/bin/bash

APP_NAME=$1
SOURCE_FOLDER=$2
API_KEY=$3

# Check that a valid number of command line arguments have been entered.
if [[ $APP_NAME = "" || $SOURCE_FOLDER = "" ]]
then
    echo Must run script with an app name and source folder name and optionally an API key for new apps.
    exit 1 
fi

echo Is the page order file in place? Enter \"no\" if not.

read response

# Exit program if the page order file is not in place.
if [ $response = "no" ]
then
    exit 1
fi

if [[ $API_KEY != "" ]]
then
    mkdir -p ~/Documents/workspace/app/data/$APP_NAME/output
fi

rm -fr ~/Documents/workspace/app/data/$APP_NAME/input/
mkdir ~/Documents/workspace/app/data/$APP_NAME/input
cd ~/Documents/workspace/app/data/$APP_NAME
rm ~/Downloads/$SOURCE_FOLDER/*-Home_*.html
cp -r ~/Downloads/$SOURCE_FOLDER/* ~/Documents/workspace/app/data/$APP_NAME/input/

if [[ $API_KEY != "" ]]
then
    ls ~/Documents/workspace/app/data/$APP_NAME/input > ~/Documents/workspace/app/data/$APP_NAME/order.txt
fi

cd ~/Documents/workspace/app/data/$APP_NAME/input
. ~/Documents/workspace/app/data/$APP_NAME/order.txt

if [[ $API_KEY != "" ]]
then
    cat > ~/Documents/workspace/app/data/$APP_NAME/$APP_NAME.ini << EOF
[IO]
source.directory=~/Documents/workspace/app/data/$APP_NAME/input/
destination.directory=~/Documents/workspace/app/data/$APP_NAME/output/
lib.directory=~/Documents/workspace/app/libraries_v2/
header.html.file=
logo.image.file=
firebase.apikey=$API_KEY
icon.app.name=

[Style]
banner.color=
EOF
fi

firebase logout
firebase login

if [[ $API_KEY != "" ]]
then
    cd ~/Documents/workspace/app/data/$APP_NAME/
    firebase init hosting
fi

/usr/bin/python -u ~/Documents/workspace/app/src/confl_to_1page_app_v2.py
~/Documents/workspace/app/data/$APP_NAME/$APP_NAME.ini

# Remove the ?height= from the URLs in index.html
sed -i '' 's/\?height=250//g' ~/Documents/workspace/app/data/$APP_NAME/output/index.html

cp -R ~/Documents/workspace/app/data/$APP_NAME/output/ ~/Documents/workspace/app/data/$APP_NAME/public

cd ~/Documents/workspace/app/data/$APP_NAME/
firebase deploy

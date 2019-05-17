if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

if ! [ -x "$(command -v nginx)" ]; then
  echo 'Error: nginx is not installed.' >&2
  apt-get update
  apt-get install nginx
  echo "===========Please run the program again because we currently installed nginx============ "
else
  site=$1

  mkdir /var/www/$site
  mkdir /var/www/$site/html

  chown -R www-data:www-data /var/www/$site/html

  dpkg -s nginx &> /dev/null

fi

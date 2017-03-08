# Helpful notes about deployment.
- Combine, minify, and gzip CSS files. 
- Combine, minify, and gzip JS files.
- You can use `gzip -9 filename.css`. The `-9` provides the best compression.
- Zopfli https://github.com/obp/zopfli developed by Google is more powerful and may one day be integrated with this project.
- Upload these two files to S3 and make the files public http://www.rightbrainnetworks.com/blog/serving-compressed-gzipped-static-files-from-amazon-s3-or-cloudfront/
- AWS Cloudfront is a CDN that can be linked to your S3 bucket. A Content Delivery Network (CDN) places the data closer to the end user by storing your files all over the world.
- Enable file Caching so that browsers do not need to download the files every time the page loads. https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching#defining-optimal-cache-control-policy
- Check your site speed with pingdom or other service https://tools.pingdom.com/#!/c1UXFm/https://kw4udfbos9.execute-api.us-west-2.amazonaws.com/production

# Development

# Prerequisite for npm powered automation
- Install node package manager (npm) on your machine.
- Place npm on the system path.

# Setup Sass and SCSS Transpiler
- Download and Install Ruby http://www.ruby-lang.org/en/downloads/
- Setup system path for Ruby
- At command prompt enter `gem install sass` to install sass.
- If you are using an IDE like PyCharm you can setup a File Watcher https://www.jetbrains.com/help/pycharm/2016.3/transpiling-sass-less-and-scss-to-css.html#intro
- Configuring File Watcher output path http://stackoverflow.com/a/36038914/1783439

# Combine Javascript files into one and minify with uglifyjs 
- Open command line as Administrator.
- Run `npm install -g uglify-js -g` the `-g` install uglify-js globally.
- Run `npm list -g --depth=0` to confirm installation `--depth=0` prevents all of the dependencies from being listed.
- You can manually run `uglifyjs --compress --mangle --output combined.min.js -- {filename1}.js {filename2}.js {filename3}.js` reference: http://www.aip.im/2015/02/how-to-minify-and-merge-javascript-files-with-uglifyjs-2/
- Recommended: Setup a custom File Watcher for PyCharm or your IDE. https://www.jetbrains.com/help/pycharm/2016.3/minifying-javascript.html
- Configuring File Watcher output path http://stackoverflow.com/a/36038914/1783439
- Set this up twice. One for combined.dev.js (vue.js debugging included) and one for combined.js (vue.min.js debugging removed)

# Setup auto-minify CSS using node.js yuicompress
- Open command line as Administrator.
- Run `npm install -g yuicompressor` 
- Run `npm list -g --depth=0` to confirm installation.
- Setup a File Watcher for YUI CSS https://www.jetbrains.com/help/pycharm/2016.3/minifying-css.html
- Configuring File Watcher output path http://stackoverflow.com/a/36038914/1783439

# Setup node-zopfli to compress combined CSS and JS files for Production
- Zopfli Compresses gzip files 5% better than gzip. To achieve the 5% it takes 100x longer than gzip. That is fine for us since we are not doing on-the-fly or just-in-time compression. https://www.npmjs.com/package/node-zopfli
- Requires Python 2.7 and either GCC (Unix) or Visual Studio Express (Windows)
- To install `gcc` on Windows via MinGW use this https://yichaoou.github.io/tutorials/software/2016/06/28/git-bash-install-gcc
- Open command line as Administrator.
- Run `npm install -g node-zopfli`
- Run `npm list -g --depth=0` to confirm installation.
- Navigate to <path to>/npm/node_modules/node-zopfli/zopfli on your machine.
- Run `gcc src/zopfli/*.c -O2 -W -Wall -Wextra -Wno-unused-function -ansi -pedantic -lm -o zopfli`
- An executable file named `zopfli` (linux) or `zopfli.exe` (windows) should now appear in your folder.
- Setup two Custom File Watchers with zopfli for CSS and JS.  Use combined.min.css and combined.js (production) 
- Configuring File Watcher output path http://stackoverflow.com/a/36038914/1783439

# Testing with Flask-Testing, Selenium, Google chromedriver, Mozilla geckodriver
- `pip install selenium`
- Google chromedriver https://sites.google.com/a/chromium.org/chromedriver/downloads
- Mozilla geckodriver https://github.com/mozilla/geckodriver/releases
- Microsoft edge webdriver https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- Microsoft Internet Explorer http://selenium-release.storage.googleapis.com/index.html
- Mac Safari webdriver https://webkit.org/blog/6900/webdriver-support-in-safari-10/

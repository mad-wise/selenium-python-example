This is a simple example of test scripts written using Python, Selenium WebDriver, PyTest and Allure. ChromeDriver is managed by webdriver-manager package. You will get the specific version chromedriver based on your OS and Chrome browser version automatically.

Pre-requisites:

Please make sure you have [Python](https://www.python.org/downloads) is installed.

Windows users make sure that the checkbox is checked as shown in the picture below:
![about_contribute_install_windows_installer](https://github.com/mad-wise/selenium-python-example/assets/102381350/487437ee-e46c-43e9-8e13-bfcce84acd3f)

Please make sure you have [PyCharm](https://www.jetbrains.com/pycharm/download) is installed.

Please make sure you have [Git](https://git-scm.com/downloads) is installed. 

Please make sure you have [Allure](https://docs.qameta.io/allure/) is installed.

Please note **Allure** requires Java to work. Please download and install JRE or JDK. To install Allure please use the following steps:

For Windows users:
  1. Install scoop https://scoop.sh/
  2. Execute **scoop install allure** in the powershell

For mac OS users:
  1. Install Homebrew https://brew.sh/
  2. Execute **brew install allure** in the terminal

macOS users: Please make sure you have **pip** installed https://pip.pypa.io/en/stable/installing/

  1. Right click on get-pip.py and select "save link as". Save get-pip.py somewhere on your computer (for example Downloads folder)
  2. Open terminal, navigate to Downloads folder (cd Downloads) and execute python3 get-pip.py

How to run your tests:

  1.	Open your PyCharm
  2.	Navigate to VCS - Git - Clone and paste repository URL
  3.	Select "New Window" option.
  4.	Click on "Terminal" at the bottom of the page
  5.	For Windows users, type in **pip install pipenv** and press Enter
  6.	For mac OS users, type in **pip3 install pipenv** and press Enter
  7.	Type in **pipenv install selenium** and press Enter
  8.	Type in **pipenv install pytest** and press Enter
  9.	Type in **pipenv install allure-pytest** and press Enter
  
Navigate to "Edit Configurations.." at the top right of the PyCharm

Click on "+" (Add New Configuration). Select pytest as on the screenshot below.

![68747470733a2f2f692e706f7374696d672e63632f4d4752365639514d2f53637265656e2d53686f742d323032302d30392d31302d61742d342d35312d30302d504d2e706e67](https://github.com/mad-wise/selenium-python-example/assets/102381350/9a9ed3fb-527d-451e-b4d0-a14595958875)

Your configuration should look similar to this one (use smoketest OR regressiontest):

![68747470733a2f2f692e706f7374696d672e63632f64336d665279734b2f53637265656e2d53686f742d323032302d30392d31302d61742d352d32382d32332d504d2e706e67](https://github.com/mad-wise/selenium-python-example/assets/102381350/11b07762-3243-48bb-beeb-e22134195243)

After you will run your test(s). To generate Allure reports and open them in the browser:

Windows users please do right click on run_reports_win.bat and run mac OS users please do right click on run_reports_mac.sh and run

It will automatically execute "allure serve reports" command and your Allure Report will open in the default browser

![Screen-Shot-2020-09-10-at-5-30-20-PM](https://github.com/mad-wise/selenium-python-example/assets/102381350/d0e401cd-cc3f-451e-bf41-9f613eed278d)

To stop executing "allure serve reports" command, press Ctrl + C in your PyCharm terminal.

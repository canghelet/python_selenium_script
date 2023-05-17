Hello!

This is my web automation script generated with Python and Selenium.
1. The script was created to automate browser tasks on "https://carturesti.ro/" website.
2. Installation:\
	a) Install Python bindings for Selenium using "pip install selenium";\
	b) Install Chrome WebDriver from "https://sites.google.com/chromium.org/driver/downloads" webpage;
3. Usage:\
	a) Script will be executed by using command "python python_selenium_script.py" from terminal/cmd;\
	b) When the script runs, it will automatically open Chrome browser, navigate to "https://carturesti.ro/" webpage, maximize the window, find and return all the links of the webpage;\
	c) Will automatically locate on the homepage the Search bar by ID, will enter "carti" text, perform the search by the given key and return the results on the page;\
	d) On the same page, will locate relevant books elements by XPATH, open the page for each book and add them to cart;\
	e) Page will be redirected to the homepage, script will locate and return the length of list with all elements having a specific CLASS_NAME;\
	f) It will navigate through pages by opening each button from navigation bar, redirecting to: "https://carturesti.ro/info/despre-carturesti-ro", "https://carturesti.ro/librarii", "https://carturesti.ro/blog";
 	g) Page will be redirected to the homepage and will automatically fill in and submit web form in order to subscribe to the website newsletter;\
	h) Browser will close.

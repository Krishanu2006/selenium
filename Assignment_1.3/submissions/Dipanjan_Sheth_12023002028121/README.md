My Submission
Name: Dipanjan Sheth
Enrollment Number:1223002028121
Description:-

For Assignment 1
I used the Automation Practice Form website to demonstrate different methods of identifying web elements in Selenium. First, the Chrome browser is opened using Selenium WebDriver and the given website URL is loaded. The browser is then maximized so that all elements are clearly visible. The Name field is located using By.ID with the ID "name", and the value "Dipanjan" is entered into the field using send_keys(). Next, the Gender radio buttons are located using By.NAME with the name "gender", and the first option is selected by using the click() method. After that, By.TAG_NAME is used to find all <input> elements on the webpage, and the total number of input elements is displayed. The By.CLASS_NAME locator is then used to identify an element using its CSS class, such as "widget-content". Finally, By.LINK_TEXT is used to locate the Apple link by its visible text, and the link text is printed. After completing all the operations, the program waits for a few seconds and then closes the browser using driver.quit(). This assignment demonstrates how Selenium can identify and interact with web elements using different locator strategies such as ID, Name, Tag Name, Class Name, and Link Text.

............................................................................................................................

Assignment 2 — Multiple Element Identification

For Assignment 2, we use the same Automation Practice Form website to identify and work with multiple web elements at the same time. Unlike find_element(), which returns only one matching element, Selenium's find_elements() method returns a list of all matching elements. In this program, we first find all <input> elements using By.TAG_NAME and display their total number along with their type, ID, and name. Then, we identify all radio buttons using the CSS selector input[type='radio'] and display their values. The first radio button is selected using the click() method. Next, we locate all checkboxes using input[type='checkbox'], display the number and values of the checkboxes, and select the first checkbox if it is not already selected. Finally, we find all <a> elements on the webpage using By.TAG_NAME, count them, and print the text of each link. This assignment demonstrates how Selenium can locate multiple similar elements, store them in a list, iterate through them using a for loop, and perform actions such as selecting radio buttons and checkboxes.

.......................................................................................................................

For Assignment 3
we use the Automation Practice Form website to demonstrate how Selenium can locate web elements using CSS selectors. CSS selectors are useful when an element does not have a convenient ID or when we want to identify elements based on their attributes. In this program, we use selectors such as input[type='text'] to locate text input fields, input[type='radio'] to locate radio buttons, and input[type='checkbox'] to locate checkboxes. We also demonstrate wildcard CSS selectors. The ^= selector is used to find elements whose attribute value starts with a particular text, *= is used to find elements whose attribute value contains particular text, and $= is used to find elements whose attribute value ends with particular text. The program prints the elements found by each selector and selects the first checkbox. This assignment helps demonstrate how CSS selectors can provide flexible and powerful ways to locate web elements in Selenium.

...................................................................................................................

For Assignment 4, we use the Automation Practice Form website to understand how to locate child and nested elements using CSS selectors in Selenium. A child element is an element that exists inside another element. For example, the webpage contains a form, and the form contains different input fields, radio buttons, checkboxes, dropdowns, and buttons. First, we locate the main <form> element using the CSS selector form. Then, we use form.find_elements(By.CSS_SELECTOR, "input") to find the input elements inside that form. We also demonstrate the CSS child selector > using form > input, which specifically searches for elements that are direct children of the form. Finally, we locate buttons inside the form using form button. This assignment demonstrates the difference between a general descendant selector and a direct-child selector and shows how Selenium can navigate through the HTML structure of a webpage.

......................................................................................................................

video link here. https://drive.google.com/file/d/1bdpkO-5_CeQQubkI7tFe1O4BdUygtMNi/view?usp=drivesdk

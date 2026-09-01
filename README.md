# 🧪 Automated Web Testing with Selenium

> **Group 79** | Institute of Engineering & Management (IEM), New Town  
> **Course:** Selenium Web Automation

---

## 👥 Contributors

| Student Name | University Roll | Enrollment ID | Stream | Section |
| :--- | :---: | :---: | :---: | :---: |
| **Yashraj Sharma** | 04 | `12023002029115` | CSE (IoT, CS & BT) | C |
| **Suvajit Majhi** | 56 | `12023002029105` | CSE (IoT, CS & BT) | B |
| **Tanisha Pan** | 62 | `12023002029111` | CSE (IoT, CS & BT) | B |

---

## 🚀 Lab Modules & Implementation Details

### 🔹 Module 1: Foundational DOM Locators
* **Target Objective:** Extract and manipulate standard webpage controls using Selenium's primitive locator strategies.
* **Technical Execution:** Verified input forms on `testautomationpractice.blogspot.com` by injecting text with `By.ID`, toggling radio selections via `By.NAME`, querying header strings with `By.TAG_NAME`, matching exact anchor strings via `By.LINK_TEXT` (`"Apple"`), and referencing styled container classes with `By.CLASS_NAME`.
* **Demonstration:** [🎥 Watch Module 1 Recording](https://drive.google.com/file/d/1ea_nhYImdo8orjf-AMOG2eH3wglGtPEW/view?usp=sharing)

---

### 🔹 Module 2: Bulk Element Extraction & Iteration
* **Target Objective:** Programmatically locate, aggregate, and iterate through multiple matching elements using batch lookup.
* **Technical Execution:** Queried all anchor tags (`<a>`) across `testautomationpractice.blogspot.com` using `find_elements(By.TAG_NAME)`. Computed the cumulative link count and looped over the resulting collection to parse and print each element's visible text.
* **Demonstration:** [🎥 Watch Module 2 Recording](https://drive.google.com/file/d/12ioBdbEPhWcfHC4uHiXMQQRzg9gQJMeZ/view?usp=sharing)

---

### 🔹 Module 3: Pattern Matching with CSS Wildcards
* **Target Objective:** Identify dynamic and non-static UI elements sharing partial attribute patterns.
* **Technical Execution:** Configured regex-style CSS substring locators (`^=`, `*=`, `$=`) on `rahulshettyacademy.com/AutomationPractice` to reliably hook into dynamically generated IDs across checkboxes and radio inputs.
* **Demonstration:** [🎥 Watch Module 3 Recording](https://drive.google.com/file/d/1xsArkTYS268ECMxdnxLvo5uK9PVpSqJI/view?usp=sharing)

---

### 🔹 Module 4: Hierarchical DOM Traversal via Child Selectors
* **Target Objective:** Access deeply nested target elements through direct parent-to-child relationships.
* **Technical Execution:** Built strict structural CSS paths (`fieldset > label > input` and `table > tbody > tr`) to select and interact with nested form fields and table row elements across the target testing suites.
* **Demonstration:** [🎥 Watch Module 4 Recording](https://drive.google.com/file/d/1g5hsRkwEvTH64a_M6j2s53kI78cPT1uq/view?usp=sharing)

---

## 📂 Submission Guidelines & Access

* All practical walkthroughs are recorded and stored on Google Drive.
* Share settings are set to public view for evaluation purposes.

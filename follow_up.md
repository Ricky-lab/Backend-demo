## Follow up questions:
### How would you go about solving Issues around data privacy and security for our daily check-in feature and menstrual calendars

### 1. Determine what to collect before how to collect:
- `Data Minimization and Anonymization`<br>
  Principle: Collect only the data necessary for the functionality of the features.
  For daily check-ins and menstrual calendars, limit the data collection to what is strictly necessary for providing the service. Avoid collecting identifiable information unless absolutely necessary.
  Implement data anonymization techniques to ensure that the data cannot be traced back to any individual user without significant effort.

### 2. Before we try to collect:
- `Access Controls and Authentication`<br>
  Principle: Ensure that only authorized users and systems can access sensitive data.
  Implement robust authentication mechanisms (e.g., OAuth) to verify user identity.
  Use role-based access control (RBAC) to restrict access to sensitive data. For example, only the user (and perhaps a guardian, if appropriate and with consent) should have access to their own menstrual calendar and check-in data.

- `User Education and Consent`<br>
  Principle: Inform users about how their data is used and obtain their consent.
  Provide clear, accessible information to users (and guardians, where appropriate) about what data is collected, how it is used, and how it is protected.
  Obtain explicit consent from users (and guardians) for the collection and processing of their data, especially for users under the age of consent for data processing in their jurisdiction.

### 3. When we are collecting and after we collect:
- `Encryption`: Protect data at rest and in transit.<br>
    Use end-to-end encryption for data transmission between the client app and the server. This ensures that data, such as daily check-in responses or menstrual calendar details, is encrypted from the moment it leaves the user's device until it reaches your server, and vice versa.
  
- `Regular Security Audits and Compliance`: Continuously monitor and improve security measures.
- `Secure Development Practices`: Integrate security into the development lifecycle.
- ...

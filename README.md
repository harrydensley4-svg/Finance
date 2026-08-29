**Week 1 Workshop (N/A)**
- No Code Review

**Week 2 Workshop 1 (2.1) 12/09/2026:**
During this weeks code review, we dicussed linking accounts to transactions. One of the major changes that I made was to ensure that a transaction can only be cancelled if it has a pending status. This is important as once a transaction has been processed it should not be able to be cancelled. Furthermore, throughout the testing, I tried to call instances that would break the code to find problem areas such as not passing through valid phone numbers. For instance, since the phone numbers are strings (in order to keep the leading zero) if I just used a simple isinstance(phone, str) anything could be passed. Instead, I had to run an additional check to ensure that the sting consisted of digits. This improved my code as it ensured that it was more robust. This helped me to understand the importance of trying to find edge cases that would break the code so that I could try and fix them. 

**Week 3 Workshop 1 (3.1) 19/09/2026**
During this weeks code review, I recieved feedback around encapsulation. To improve upon this I made most of my class attributes private. This more closely resembles actual financial software as it is important to restrict who can change values. Since the attributes were made private, I had to use getters and setters to view and change them. This is especially important as it allows for validation to be performed before an attribute is modified. Additionally, we also looked at the relationships between classes. In accordance with this, I made it so a client could add or remove accounts and stored these accounts in a list. Furthermore, I also made it so the clients could select their preferred branch using a setter. All these changes allowed for my code to better reflect the actual functionalities of a banking system. 

**Week 4 Workshop (N/A)**
- Extension Week
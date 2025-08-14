class Page:
    def __init__(self, heading, body):
        self.heading = heading
        self.body = body

    def create_page(self):
        html = f"<h1>{self.heading}</h1><p>{self.body}</p>"
        return html

class Contact(Page):
    def __init__(self, heading, body, email):
        super().__init__(heading, body)
        self.email = email 
    def create_button(self):
        return f"<button>{self.email} Contact Now!</button>"

contact = Contact("Contact us", "Please give us your feedback", "trifa@gmail.com")
print(contact.create_button())
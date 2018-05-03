'''
#: Written by KFH: karshi.hasanov@utoronto.ca
#: Date: April 8, 2018
#: Description: Python Code for my Contacts Info.
#: JSON to Python Conversion:
#: --------------------------------
#:  Object {...} ---> Dictionary
#:  Array  [...] ---> List or Tuple
#:  Number(Intger) ---> Integer
#:  Real Numbers   ---> Float
#:  null ---> None
#:  true, false ---> True, False
#:  Strings ---> Strings
#: --------------------------------
#: Last Modified: April 12, 2018
#: - More fields added.
#: - To validate a JSON file visit: https://jsonlint.com/
'''
import datetime
import json


class KFH_Contacts:
    # fileName = 'KFH_Contacts.json'

    def __init__(self, fileName='KFH_Contacts.json'):
        self.file = fileName
        self.data = None
        self.ID = None  # The ID of the entire Contact file
        self.id = None  # The id of each contact
        self.firstName = ''
        self.lastName = ''
        self.fullName = ''
        self.phone = []  # [ {home_phone}, {work_phone}, ...]
        self.email = []  # [ { personal_email}, {business_email}, ...]

        #['type','street','city','state/province','postalCode','country']
        self.address = []
        self.state = self.province = None
        self.website = []  # ['type', 'site']
        self.categories = 'all'
        self.notes = None
        self.address_info = None
        self.status = True

        # Reading the JSON file
        try:
            with open(self.file) as file:
                self.data = json.load(file)

        except FileNotFoundError as e:
            # print(e)
            print("Error: The file '{}' not found!".format(self.file))

        # Run this block only if there were no problems in "try"
        else:
            self.ID = self.data['ID']



    def addPerson(self):
        self.people = self.data['all']
        self.new_person = {}
        Keys = ['id', 'firstName', 'lastName', 'phone', 'email', 'address', 'website', 'notes']
        Values = [self.id, self.firstName, self.lastName, self.phone, self.email,
                  self.address, self.website, self.notes]

        self.new_person = dict(zip(Keys, Values))
        self.people.append(self.new_person)

    def setID(self):
        # First we want to update the JSON file ID:
        self.updateID()
        # Then we assign its value to 'id' of a newly created personal contact info:
        self.id = self.ID

    def setFirstName(self, firstName="Roy"):
        self.firstName = firstName

    def setLasttName(self, lastName="Masters"):
        self.lastName = lastName

    def setPhoneNumber(self, phone_type='home', phone_number='1 541 955-1791'):
        type, number = phone_type, phone_number
        Keys = ['type', 'number']
        Values = [type, number]
        new_phone = dict(zip(Keys, Values))
        self.phone.append(new_phone)

    def setEmail(self, type='business', address='fhu@aol.com'):
        type, address = type, address
        Keys = ['type', 'address']
        Values = [type, address]
        new_email = dict(zip(Keys, Values))
        self.email.append(new_email)

    def setAddress(self, street='', city='', postalCode='', province='', state=None, country=''):
        street = "PO Box 1000"
        city = "Grants Pass"
        postalCode = "97528"
        state = "OR"
        country = "USA"
        if (state == None):
            province = ''
            Keys = ['street', 'city', 'postalCode', 'province', 'country']
            Values = [street, city, postalCode, province, country]
        else:
            Keys = ['street', 'city', 'postalCode', 'state', 'country']
            Values = [street, city, postalCode, state, country]
        new_address = dict(zip(Keys, Values))
        self.address.append(new_address)

    def setWebsite(self, type='business', site='www.fhu.com'):
        type, site = type, site
        Keys = ['type', 'site']
        Values = [type, site]
        new_website = dict(zip(Keys, Values))
        self.website.append(new_website)

    def setNotes(self, notes=None):
        self.notes = notes

    def updateID(self):
        # This will increment the current value of the JSON file ID to "1".
        self.ID = self.ID + 1
        # Then updates the its value.
        self.data['ID'] = self.ID

    def updateDate(self):
        today = datetime.datetime.today()
        # Moth Day, Year
        self.data['date'] = today.strftime("%B %d, %Y")

    def addContact(self):
        # Remember: All these "set" fucntions take arguments !!!
        # For testing purpose, I am not using the arguments.
        self.updateDate()
        self.setID()
        self.setFirstName()
        self.setLasttName()
        self.setPhoneNumber()
        self.setEmail()
        self.setAddress()
        self.setWebsite()
        self.setNotes()
        self.addPerson()

        # Saving as a JSON file:
        with open("Test_Contacts.json", 'w') as f:
            json.dump(self.data, f, indent=2)

        # I will test this one later
        # while (self.status):
        #     name = input("Please enter a name")
        #     print(name)
        #     answer = input("Are you happy with this ? ('Yes/No') ")
        #     respond = ['Yes', 'yes', 'Y', 'y']
        #     if answer in respond:
        #         self.status = False
        # print("Good")
    def removeDuplicates(self, List):
        """
        The function removes the duplicate items in a list.
        The items must be a dictionary type (i.e. {'key':'value'})
        We call this function just before creating the JSON file, so
        we don't end up with multiple phones or emails with the same value.
        """
        return [dict(t) for t in set([tuple(d.items()) for d in List])]
        # return [i for n, i in enumerate(List) if i not in List[n + 1:]]


def main():

    c = KFH_Contacts()
    c.addContact()

    print(c.data)


if __name__ == '__main__':
    main()

import string
import random


class UtilitiesHelper(object):

    def __init__(self):
        pass

    male_first_names = ['Richard', 'Scott', 'Matthew', 'James', 'Chris', 'Bob', 'Nicholas', 'Darren', 'Rob', 'George',
                        'Luke', 'John', 'Joe', 'Homer', 'Tom', 'Robert', 'Rupert', 'Oliver', 'Harry', 'Charlie', 'Noah'
                        , 'Jack', 'Alfie', 'Jack', 'Leo', 'Jacob', 'Freddie', 'Oscar', 'Theo', 'Archie', 'Arthur','Logan',
                        'Joshua', 'Thomas', 'Max', 'Lucas', 'Ethan', 'William', 'Isaac', 'Mason', 'Riley', 'Harrison',
                        'Finley', 'Tommy', 'Teddy', 'Dylan', 'Daniel', 'Tyler', 'Adam', 'Joseph', 'Alexander', 'Elijah',
                        'Jayden', 'Louie', 'Arlo', 'Hunter', 'Jake', 'Jaxon', 'Reggie', 'Frankie', 'Harley', 'Albie',
                        'Harvey', 'Toby', 'Edward', 'Lewis', 'Sebastian', 'Theodore', 'Rory', 'Ollie', 'Alex', 'Reuben',
                        'Benjamin', 'Luca', 'Ryan', 'Liam', 'Bobby', 'Carter', 'Samuel', 'Roman', 'Louis', 'David',
                        'Hugo', 'Jude', 'Jenson', 'Ronnie', 'Zachary', 'Blake', 'Jackson', 'Ezra', 'Kai', 'Luke', 'Caleb',
                        'Connor', 'Elliott', 'Leon', 'Jamie', 'Grayson', 'Nathan', 'Stanley', 'Finn', 'Elliot', 'Albert',
                        'Aaron', 'Gabriel', 'Cameron', 'Ben', 'Dexter', 'Oakley', 'Eli']
    female_first_names = ['Chloe', 'Harmony', 'Claire', 'Sam', 'Cat', 'Victoria', 'Rachel', 'Sarah', 'Debbie',
                        'Scarlet', 'Olivia', 'Amelia', 'Isla', 'Ava', 'Emily', 'Sophie', 'Sophia', 'Grace', 'Mia', 'Poppy',
                        'Ella', 'Lily', 'Evie', 'Isabelle', 'Isabella', 'Ivy', 'Freya', 'Harper', 'Willow', 'Charlotte',
                        'Jessica', 'Rosie', 'Daisy', 'Alice', 'Elsie', 'Sienna', 'Florence', 'Evelyn', 'Phoebe', 'Aria', 'Ruby', 'Esme',
                        'Scarlett', 'Matilda', 'Sofia', 'Millie', 'Eva', 'Layla', 'Chloe', 'Luna', 'Maisie', 'Lucy',
                        'Erin', 'Eliza', 'Ellie', 'Mila', 'Imogen', 'Bella', 'Lola', 'Molly', 'Maya', 'Violet',
                        'Lilly', 'Holly', 'Thea', 'Emilia', 'Hannah', 'Penelope', 'Harriet', 'Georgia', 'Emma', 'Lottie',
                        'Nancy', 'Rose', 'Amber', 'Elizabeth', 'Gracie', 'Zara', 'Darcie', 'Summer', 'Hallie', 'Aurora',
                        'Ada', 'Anna', 'Orla', 'Robyn', 'Bonnie', 'Abigail', 'Darcy', 'Eleanor', 'Arabella', 'Lexi', 'Clara',
                        'Heidi', 'Annabelle', 'Jasmine', 'Nevaeh', 'Victoria', 'Myla', 'Maria', 'Julia', 'Annie', 'Darcey',
                        'Zoe', 'Felicity', 'Iris', 'Niamh', 'Kim', 'Georgina', 'Tanya']
    surnames = ['Smith', 'Jones', 'Button', 'Miller', 'Turner', 'Hollywood', 'Simms', 'Burgin', 'McGettigan', 'Bullet',
                'Brown', 'Hall', 'Palmer', 'Green', 'Clark', 'Quinn', 'Harper', 'Johnson', 'Owen', 'Ross', 'Carr', 'Allen', 'Hunter', 'Wilson',
                'Davis', 'Rogers', 'Anderson', 'Jennings', 'Day', 'Jackson', 'Hewitt', 'Morgan', 'Kelly', 'Rowe', 'Reynolds', 'Austin', 'Harding',
                'Hammond', 'Buckley', 'Burgess', 'Glover', 'Riley', 'Willis', 'Richardson', 'Hawkins', 'Doyle', 'Wells', 'Perry', 'Heath', 'Bates',
                'Steele', 'Johnston', 'Holland', 'Barnett', 'Jones', 'Spencer', 'Barry', 'Hayes', 'Grant', 'Gardner', 'Goodwin', 'Cox', 'Chambers',
                'Barrett', 'Warren', 'Little', 'Coates', 'Archer', 'Mann', 'Howell', 'Dale', 'Oliver', 'Wheeler', 'Andrews', 'Waters', 'Moss',
                'Briggs', 'West', 'Blake', 'Patterson', 'Higgins', 'Francis', 'Barber', 'Frost', 'Griffin', 'Middleton', 'Murphy', 'Lambert',
                'Kent', 'George', 'Marsh', 'Reed', 'Page', 'Stone', 'Dean', 'Booth', 'Roberts', 'Elliott', 'Bailey', 'Harris', 'Bolton', 'Morton',
                'Sanders', 'Joyce', 'James', 'Smith', 'Hill', 'Douglas', 'Thomson', 'Khan']
    domains = ['gmail', 'yahoo', 'hotmail', 'sky', 'aol', 'mail']
    domain_ext = ['com', 'co.uk']
    gender = ['male', 'female']
    city = ['Leeds', 'Liverpool', 'London', 'Glasgow', 'Edinburgh',
                'Cardiff', 'Birmingham', 'Bristol', 'Manchester',
                'Sheffield', 'Leicester', 'Coventry', 'Bradford', 'Belfast',
                'County Down', 'Nottingham', 'Kingston-upon-Hull',
                'Newcastle upon Tyne', 'Stoke - on - Trent', 'Southampton', 'Derby',
                'Portsmouth', 'Brighton', 'Plymouth', 'Northampton', 'Reading'
                'Luton', 'Wolverhampton', 'Bolton', 'Aberdeen', 'Bournemouth',
                'Norwich', 'Swindon', 'Swansea', 'Milton Keynes', 'Southend - on - Sea',
                'Middlesbrough', 'Peterborough', 'Sunderland', 'Warrington',
                'Huddersfield', 'Slough', 'Oxford', 'York', 'Poole',
                'Ipswich', 'Telford', 'Cambridge', 'Dundee', 'Gloucester',
                'Blackpool', 'Birkenhead', 'Watford', 'Sale', 'Colchester',
                'Newport', 'Solihull', 'High Wycombe', 'Exeter', 'Gateshead',
                'Blackburn', 'Cheltenham', 'Maidstone', 'Chelmsford', 'Salford',
                'Basildon', 'Doncaster', 'Basingstoke', 'Worthing', 'Eastbourne',
                'Crawley', 'Rochdale','Rotherham', 'Stockport',
                'Gillingham', 'Sutton Coldfield', 'Woking', 'Wigan', 'Lincoln',
                'Oldham', 'Wakefield', 'St Helens', 'Worcester',
                'Bath', 'Preston', 'Raleigh', 'Barnsley', 'Stevenage',
                'Hastings', 'Southport', 'Darlington', 'Bedford', 'Halifax',
                'Hartlepool', 'Chesterfield', 'Nuneaton', 'Grimsby',
                'Weston - super - Mare', 'Chester', 'St Albans']
    county = ['West Yorkshire', 'Merseyside', 'Greater London', 'Scotland', 'Scotland',
                'Wales', 'West Midlands', 'South West', 'Greater Manchester',
                'South Yorkshire', 'Leicestershire', 'West Midlands', 'West Yorkshire', 'County Antrim',
                'Northern Ireland', 'Nottinghamshire', 'East Riding of Yorkshire',
                'Tyne and Wear', 'Staffordshire', 'Hampshire', 'Derbyshire',
                'Hampshire', 'East Sussex', 'Devon', 'Northamptonshire', 'Berkshire'
                'Bedfordshire', 'West Midlands', 'Greater Manchester', 'Scotland', 'Dorset',
                'Norfolk', 'Wiltshire', 'Wales', 'Buckinghamshire', 'Essex',
                'North East', 'Cambridgeshire', 'Tyne and Wear', 'Cheshire',
                'West Yorkshire', 'Berkshire', 'Oxfordshire', 'North Yorkshire', 'Dorset',
                'Suffolk', 'Shropshire', 'Cambridgeshire', 'Scotland', 'Gloucestershire',
                'Lancashire', 'Merseyside', 'Hertfordshire', 'Greater Manchester', 'Essex',
                'Wales', 'West Midlands', 'Buckinghamshire', 'Devon', 'Tyne and Wear',
                'Lancashire', 'Gloucestershire', 'Kent', 'Essex', 'Greater Manchester',
                'Essex', 'South Yorkshire', 'Hampshire', 'West Sussex', 'East Sussex',
                'West Sussex', 'Greater Manchester','South Yorkshire', 'Greater Manchester',
                'Kent', 'West Midlands', 'Surrey', 'Greater Manchester', 'Lincolnshire',
                'Greater Manchester', 'West Yorkshire', 'Merseyside', 'Worcestershire',
                'Somerset', 'Lancashire', 'Essex', 'South Yorkshire', 'Hertfordshire',
                'East Sussex', 'Merseyside', 'County Durham', 'Bedfordshire', 'West Yorkshire',
                'County Durham', 'Derbyshire', 'Warwickshire', 'North East Lincolnshire',
                'Somerset', 'Cheshire', 'Hertfordshire']
    occupation = ['Teacher', 'Police Officer', 'Doctor', 'Nurse', 'Clerk', 'Shop assistant', 'Scientist',
                  'Bus driver', 'Project Manager', 'Chef', 'Astronaut', 'Accountant', 'Manager', 'Project Manager',
                  'Teacher', 'Director', 'Consultant', 'Administrator', 'Solicitor', 'Account Manager', 'PA', 'Office Manager',
                  'Analyst', 'Engineer', 'Sales Manager', 'Doctor', 'Software Engineer', 'Business Analyst', 'Managing Director',
                  'Personal Assistant', 'Marketing Manager', 'Operations Manager', 'IT Manager', 'General Manager', 'Software Developer',
                  'Accounts Assistant', 'Secretary', 'Team Leader', 'Business Development Manager', 'Developer', 'Graphic Designer',
                  'Lecturer', 'Architect', 'HR Manager', 'Receptionist', 'Assistant Manager', 'Buyer', 'Design Engineer', 'Associate',
                  'Marketing Executive', 'Product Manager', 'Web Developer', 'Management Accountant', 'Programmer', 'Sales', 'Financial Controller',
                  'Finance Manager', 'Quantity Surveyor', 'Designer', 'Technician', 'Sales Director', 'Sales Assistant', 'Project Engineer', 'Electrician',
                  'Pharmacist', 'Sales Executive', 'Marketing Assistant', 'Store Manager', 'Supervisor', 'Nurse', 'Recruitment Consultant',
                  'Production Manager', 'Lawyer', 'Senior Engineer', 'Dentist', 'GP', 'Account Executive', 'Web Designer', 'Driver',
                  'Senior Consultant', 'Social Worker', 'Assistant Operations Director', 'CEO', 'Credit Controller', 'Senior Manager',
                  'Pilot', 'Plumber', 'Editor', 'Finance Director', 'Barrister', 'Mechanical Engineer', 'Hr Advisor', 'Programme Manager',
                  'Assistant Accountant', 'Executive Assistant', 'Scientist', 'Estimator', 'Marketing Director', 'Vice President', 'Trader',
                  'Commercial Manager', 'Researcher', 'Trainer', 'Auditor', 'Technical Manager', 'Hr Administrator', 'Graduate',
                  'Financial Analyst', 'Branch Manager', 'Area Manager', 'Sailor']
    all_users = []

    def display_all_users(self):
        it = len(self.all_users)
        for i in range(0, it):
            print(self.all_users[i])
            ##print('\n')

    def return_all_users(self):
        return self.all_users

    def clear_all_users(self):
        self.all_users.clear()

    def generate_group_of_test_users(self, number):
        ## creates a group of x test users
        email_number = 0
        for i in range(0, number):
            user = self.generate_one_user(str(email_number))
            email_number += 1
            self.all_users.append(user)

    def generate_one_user(self, email_number):
        ## creates one test user, male or female
        ## returns firstname, surname, gender, age, location, occupation, emailaddress(unique) password

        counter = random.randint(0, 97)
        user_age = random.randint(19, 66)
        user_male_first_name = self.male_first_names[random.randint(0, 109)]
        user_female_first_name = self.female_first_names[random.randint(0, 109)]
        user_surname = self.surnames[random.randint(0, 109)]
        user_email_domain = self.domains[random.randint(0, 5)]
        user_email_ext = self.domain_ext[random.randint(0, 1)]
        user_gender = self.gender[random.randint(0, 1)]
        user_occupation = self.occupation[random.randint(0, 110)]
        user_city = self.city[counter]
        user_county = self.county[counter]
        user_password = ''.join(random.choices(string.ascii_letters, k=20))

        if user_gender == 'male':
            first_name = user_male_first_name
        else:
            first_name = user_female_first_name

        user_email_address = self.generate_valid_email_address(first_name, user_surname, email_number, user_email_domain, user_email_ext)
        new_user = [first_name, user_surname, user_gender, user_age, user_city, user_county, user_occupation, user_email_address, user_password]

        return new_user

    def generate_valid_email_address(self, first_name, surname, email_number, domain, domain_ext):
        email_address = first_name + surname + str(email_number) + '@' + domain + '.' + domain_ext
        return email_address

    def generate_valid_password(self):
        password_length = 20
        password_string = ''.join(random.choices(string.ascii_letters, k=password_length))
        return password_string

    def generate_random_email_and_password(self, domain=None, email_prefix=None):

        if not domain:
            domain = 'gmail.com'
        if not email_prefix:
            email_prefix = 'testuser'

        random_email_string_length = 10
        random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))

        email = email_prefix + '_' + random_string + '@' + domain

        password_length = 20
        password_string = ''.join(random.choices(string.ascii_letters, k=password_length))
        random_info = {'email': email, 'password': password_string}
        print(random_info)
        return random_info

    def generate_random_first_and_last_name(self, f_name_pre='test f ', l_name_pre='test l '):
        random_f_name = f_name_pre + ''.join(random.choices(string.ascii_lowercase, k=7))
        random_l_name = l_name_pre + ''.join(random.choices(string.ascii_lowercase, k=7))

        return {'f_name': random_f_name, 'l_name': random_l_name}

    def generate_random_coupon_code(self, suffix=None, length=10):
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if suffix:
            code += suffix
        return code


if __name__ == '__main__':
    #print(location.__len__())
    bob = UtilitiesHelper()
    bob.generate_group_of_test_users(100)
    bob.display_all_users()

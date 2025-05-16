# Email_validator 

#Employee details
emp_details = [
    {"emp_name": " Alice John ", "email_id": "Alice.J@company.com"},
    {"emp_name": "Bob Smith", "email_id": "bob.smith@company.com"}, 
    {"emp_name": "   Carol Lee", "email_id": "carol.lee@otherdomain.com"}]

for emp in emp_details:
    emp_name = emp["emp_name"].strip()  
    email_id = emp["email_id"].strip().lower()

    indx = email_id.index("@")
    domain = email_id[indx:]
    email_id= email_id.replace(domain, "@altimerik.com")

    if not email_id.startswith(emp_name[0].lower()):
        print(f"Invalid email format for {emp_name} doesn't start with name.")
        continue

    if "@altimerik.com" not in email_id:
        print(f"Invalid email format for {emp_name}:{email_id}")
        continue
   
    #generate username
    parts = emp_name.lower().split()
    if len(parts) >=2:
        username = parts[0] + "." + parts[1] 
    else:
        username = parts[0]

    #Output
    print(f"Name: {emp_name} | Email: {email_id} | Username: {username}")


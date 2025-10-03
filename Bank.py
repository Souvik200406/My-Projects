import datetime
import random
import calendar
class bank_private_details():
    bank_name="Bank Of Trust"
    bank_id="#100AC52"
    bank_branches="500"
    bank_headquarter="Mumbai"
    bank_sub_hq1="Kolkata"
    bank_finance_region="New Delhi"
    bank_contact_no="9000582101"

    def bank_private_details_name(self):

        print("Welcome To",bank_private_details.bank_name)
        print("We Ensure The Trust Of Our Users\n")
        print("PROTECTING USER ID & DATA IS OUR TOP PRIORITY")

    def bank_private_details_id(self):
        print("Our id is:",bank_private_details.bank_id)
    
    def bank_private_details_branch_hq_fin_contact(self):
        print("For more further information please select any option:-\n" \
        "1-Number of Branches\n" \
        "2-Headquarter\n" \
        "3-Sub Headquarter\n" \
        "4-Financial Hub\n" \
        "5-Contact No.")

        Number_of_branches=self.bank_branches
        Headquarter=self.bank_headquarter
        Sub_headquarter=self.bank_sub_hq1
        Financial_hub=self.bank_finance_region
        contact_no=self.bank_contact_no

        user_personal_choice=int(input("Please Select Any Above Option:"))
        
        while True:

            if user_personal_choice==1:
                print("Total Number of Branches our Bank have:",Number_of_branches)
                break
            elif user_personal_choice==2:
                print("Our  Headquarter Situated In:",Headquarter)
                break
            elif user_personal_choice==3:
                print("Our Sub Headquarter Situated In:",Sub_headquarter)
                break
            elif user_personal_choice==4:
                print("Our Financial Hub Situated In:",Financial_hub)
                break
            elif user_personal_choice==5:
                print("For Contacting With Our Team:",contact_no)
                break
            else:
                print("Wrong Input,Please Try Again!")
                break

                again=input("Do You Want To Check Again?,Please Select Y or N:")
                if again.lower()!="y":
                    print("Thanks Glad To Assist You!")
                    break

class bank_account_details_of_use():
    def __init__(self,acc_no,acc_name,acc_pass,acc_father_name,acc_mother_name,acc_id,acc_ph_no,acc_branch,acc_area,acc_area_pin_code,acc_total_balance,acc_email_id,acc_address,acc_user_age,acc_user_gender):

        self.__acc_no=acc_no
        self.__acc_name=acc_name
        self.__acc_pass=acc_pass
        self.acc_user_age=acc_user_age
        self.acc_user_gender=acc_user_gender
        self.__acc_father_name=acc_father_name
        self.__acc_mother_name=acc_mother_name
        self.acc_id=acc_id
        self.__acc_ph_no=acc_ph_no
        self.acc_branch=acc_branch
        self.acc_area=acc_area
        self.acc_area_pin_code=acc_area_pin_code
        self.__acc_total_balance=acc_total_balance
        self.__acc_email_id=acc_email_id
        self.__acc_address=acc_address
        self.__acc_transaction=[]
        
    def user_accno_pass_show(self):

        print("For Account No please Give Your Name,Account Id,PhoneNo:\n")

        print("Please Select You Want To See:\n" \
        "1.Account No.\n" \
        "2.Account Password\n")

        while True:
                 user_account_phone_no_sec1=self.__acc_ph_no
                 user_account_no_sec1=self.__acc_no
                 user_account_pass_sec1=self.__acc_pass

                 user_choice_option=int(input())
                 if user_choice_option==1:
                    print("Give Your Name, ID & Phone No:")

                    user_account_name=input("Enter Your Name:")
                    user_account_no_check_user_id_section=int(input("Enter Your Account Id:"))
                    user_inputed_ph_no=int(input("Ph No:"))

                    if user_account_no_check_user_id_section==self.acc_id and user_inputed_ph_no==user_account_phone_no_sec1 and user_account_name==self.__acc_name:
                 
                        print("Your Account Number Is:",user_account_no_sec1)
                        break

                    else:
                        print("Id or Phone no or Name is invalid")
        
                 elif user_choice_option==2:
            
                    print("Give Your Name,ID & Phone No:")

                    user_account_name=input("Enter Your Name:")
                    user_account_no_check_user_id_section=int(input("Enter Your Account Id:"))
                    user_inputed_ph_no=int(input("Ph No:"))

                    if user_account_no_check_user_id_section==self.acc_id and user_inputed_ph_no==user_account_phone_no_sec1 and user_account_name==self.__acc_name:
                 
                        print("Your Account Number Is:",user_account_pass_sec1)
                        break

                    else:
                        print("Id or Phone no or Name is invalid")

                        print("Want To Retry again?")

                        again_retry=input("Retry Y or N:")
                        if again_retry.lower()!="y":
                            break

#Day 21(Practice, Same Previous One)

    def user_account_pass_phno_reset(self):

        print("Hello Sir,Do You Want To Change Your Account Pass or Phone Number?")

        while True:
            user_pass_reset=self.__acc_pass
            user_yes_no=input("Yes/No:")

            if user_yes_no.lower() not in ["yes","y"]:
                print("No Change have been done!!!")
                return
            else:
                print("Choose The One You Want To Change:" \
            "1.Account Password" \
            "2.Account Phone Number" \
            "3.Exit")

            user_acc_pass_number_choice_var=int(input(":"))

            if user_acc_pass_number_choice_var==1:
                    print("Please Enter Your Old Password:")
                    while True:
                        try:
                            old_pass_user=int(input(":"))
                            break
                        except ValueError:
                            print("Password Must Be Digits Only .Try Again")

                    if old_pass_user!=user_pass_reset:
                        print("Password Doesn't Match Please Enter Correct Password!!")
                        continue
                   
                    else:
                        while True:

                            new_pass=(input("New Password:"))
                            new_pass_confirm=(input("Confirm Password"))

                            if new_pass!=new_pass_confirm:
                                print("Password Does not match!")
                                
                            elif len(new_pass)<5:
                             print("Password Is Too Short")
                             
                            else:
                                self.__acc_pass=new_pass
                                print("Your Password Changed Succesfully")
                                break
                        
            elif user_acc_pass_number_choice_var==2:
                print("Please Enter Your Old Phone Number:")
                while True:
                    try:
                        old_phone_no_user=int(input(":"))
                        break
                    except ValueError:
                        print("Digits Only")

                if old_phone_no_user!=self.__acc_ph_no:
                    print("Phone Number Doesn't Match")
                    continue
                
                else:

                    while True:
                     new_phone_no=(input("New Number:"))
                     new_phone_no_confirmation=(input("Confirm Number:"))

                     if new_phone_no!=new_phone_no_confirmation:
                        print("Phone Number Does Not Match !")
                        
                     elif len(new_phone_no)!=10:
                        print("PHONE NUMBER MUST HAVE 10 DIGITS")
                        
                     else:
                        self.__acc_ph_no=new_phone_no
                        print("Succefully Changed")
                        break
            
            elif user_acc_pass_number_choice_var==3:
                print("Thanks For Using Our System!")
                break

            else:

                print("Invalid Input Please Use Correct Input!")
        
            print("Do you want to check again?")
            user_choice_reset_section=input("Y/N:")

            if user_choice_reset_section.lower()!="y":
                print("Thanks For Using Our System!")
                break

    @property
    def account_data_name(self):
        return self.__acc_name

    @account_data_name.setter
    def account_data_name(self):
        print("For Changing Name: ")
        name_user=input("Enter New Name:")
        name_pass_user=int(input("Enter Password To Change Name:"))

        if name_pass_user==self.__acc_pass:
            if all(c.isalpha()or c.isspace() for c in name_user):
                print("Succefully Changed")
                self.__acc_name=name_user
            else:
                print("Special Character'$','*','@','&' or Numbers are not allowed" )
        else:
            print("Please Enter Correct Password To Change Your Name!")


    @property
    def account_father_name(self):
        return self.__acc_father_name

    @account_father_name.setter
    def account_father_name(self):
        print("For Changing Father's Name: ")
        name_user_father=input("Enter New Name:")
        name_pass_user_for_father=int(input("Enter Password To Change Name:"))

        if name_pass_user_for_father==self.__acc_pass:
            if all(c.isalpha()or c.isspace() for c in name_user_father):
                print("Succefully Changed")
                self.__acc_father_name=name_user_father
            else:
                print("Special Character'$','*','@','&' or Numbers are not allowed" )
        else:
            print("Please Enter Correct Password To Change Your Father Name!")


    @property
    def account_mother_name(self):
        return self.__acc_mother_name

    @account_mother_name.setter
    def account_mother_name(self):
        print("For Changing Mother's Name: ")
        name_user_mother=input("Enter New Name:")
        name_pass_user_mother=int(input("Enter Password To Change Name:"))

        if name_pass_user_mother==self.__acc_pass:
            if all(c.isalpha()or c.isspace() for c in name_user_mother):
                print("Succefully Changed")
                self.__acc_mother_name=name_user_mother
            else:
                print("Special Character'$','*','@','&' or Numbers are not allowed" )
        else:
            print("Please Enter Correct Password To Change Your Mother Name!")


    @property
    def account_email_id(self):
        return self.__acc_email_id

    @account_email_id.setter
    def account_email_id(self):
        print("For Changing Email: ")
        old_email=input("Old Email:")

        if old_email!=self.__acc_email_id:
            print("You added Wrong Email Please Add The Correct One")
        else:
            new_user_email=input("New Email:")
            new_user_email_confirmation=input("New Email:")

            if new_user_email==new_user_email_confirmation:
                print("E-Mail changed succesfully")
                self.__acc_email_id=new_user_email

            else:
                print("Please Try Again & Enter Correct Mail")


    @property
    def account_balance_update_add(self):
        return self.__acc_total_balance

    @account_balance_update_add.setter
    def account_balance_update_add(self):
        
        print("To Check Total Balance or Add Money:")
        print("1.Add Money"
        "2.Total Balance")

        user_balance_money_choice=int(input(":"))

        if user_balance_money_choice==1:
            print("Enter Your Account No,Id,Password To Add Money:")

            user_add_money_to_balance_acc_no=input("Your Acc No:")
            user_add_money_to_balance_pass=input("Your Password:")
            user_add_money_to_balance_id=input("Your Id:")

            if user_add_money_to_balance_acc_no==self.__acc_no and user_add_money_to_balance_pass==self.__acc_pass and user_add_money_to_balance_id==self.acc_id:
                user_added_money_amount_value=int(input("Enter The Amount:"))
                print("Please Type 'CONFIRM'  ")
                while True:
                        user_assurance=input("")
                        if user_assurance.lower()=="confirm":
                            self.__acc_total_balance+=user_added_money_amount_value
                            self.transaction_history("Deposit",user_added_money_amount_value)
                            print(user_added_money_amount_value,"is added to Your Account",self.acc_id)
                            print("Your Current Balance is:",self.__acc_total_balance)
                            break
                        else:
                            print("Please Make Sure To Type Confirm")
                        
            
    @property
    def account_address_details(self):
        return self.__acc_address

    @account_address_details.setter
    def account_address_details(self):
        print("For Changing address: ")
        address_user=input("Enter New address:")
        address_pass_user=int(input("Enter Password To Change Name:"))

        if address_pass_user==self.__acc_pass:
            if all(c.isalpha()or c.isspace() for c in address_user):
                print("Succefully Changed")
                self.__acc_address=address_user
            else:
                print("Special Character'$','*','@','&' or Numbers are not allowed" )
        else:
            print("Please Enter Correct Password To Change Your Address!")

    @property
    def account_number(self):
        return self.__acc_no
    
    @property
    def account_phone_number(self):
        return self.__acc_ph_no

    def transaction_history(self,type_of_transaction,amount):
        transaction={
            "type":type_of_transaction,
            "amount":amount,
            "date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.__acc_transaction.append(transaction)

    def  user_transaction_history(self):
        if not self.__acc_transaction:
            print("No Transaction Yet")
            return
        print("Transaction Histroy")
        for t in self.__acc_transaction:
            print(f"{t['date']} | {t['type']} | Amount:{t['amount']}")

    def deduct_balance(self,amount):
        if amount<=self.__acc_total_balance:
            self.__acc_total_balance-=amount
            self.transaction_history("Withdrawal",amount)
            return True
        else:
            return False
    
    def add_balance(self,amount):
        self.__acc_total_balance+=amount
        self.transaction_history("Deposit",amount)


#Day 22-(Practice)


class atm_registration_form():
    def __init__(self,account):
        self.account=account

    def user_atm_application_form(self):

        if self.account.acc_user_gender.lower()=='m':
            print("Hello & Welcome Mr",self.account.account_data_name,"Thanks for using",bank_private_details.bank_name)
            print("Please Proceed Further To & Fillup The Form Step By Step:")

        else:
            print("Hello & Welcome Mrs",self.account.account_data_name,"Thanks for using",bank_private_details.bank_name)
            print("Please Proceed Further To & Fillup The Form Step By Step:")
        while True:
            user_atm_form_name=input("Your Name:")
            user_atm_form_account=input("Your Account No:")
            user_atm_form_phone_number=input("Your Phone Number:")
            user_atm_form_account_id=input("Your Account Id:")
            user_atm_form_account_area_pin_code=input("Your Account Area Pin Code:")
            user_atm_form_account_address=input("Your Account Address:")
            user_atm_form_account_email_id=input("Your Email Address:")

            if user_atm_form_name==self.account.account_data_name and user_atm_form_account==self.account.account_number and user_atm_form_phone_number==self.account.account_phone_number and user_atm_form_account_id==self.account.acc_id and user_atm_form_account_area_pin_code==self.account.acc_area_pin_code and user_atm_form_account_address==self.account.account_address_details and user_atm_form_account_email_id==self.account.account_email_id:

                print("Form Submitted Succesfully!")
                break
            else:
                print("Error Values ! please give proper details which You Provided in bank account same details required!")

                again=input("Do You Want To Retry ? Type 'y' anything else is cancelled:")
                if again.lower()!='y':
                    print("Your Form Submission Cancelled.")
                    break
#DAY 23-(Practice)

class atm_details_account_of_user(bank_private_details):
    def __init__(self,account_bank,atm_id,atm_number,atm_pass,atm_cvv,atm_user_name,atm_phone_number,atm_date,atm_card_type):
        
        self.atm_id=atm_id
        self.atm_number=atm_number
        self.__atm_pass=atm_pass
        self.__atm_cvv=atm_cvv
        self.atm_user_name=atm_user_name
        self.atm_phone_number=atm_phone_number
        self.atm_date=atm_date
        self.atm_card_type=atm_card_type
#DAY 24-(Practice)
        self.account_bank=account_bank
    @property
    def user_atm_id(self):
        return self.atm_id
    
    @user_atm_id.setter
    def user_atm_id(self):

        print("Welcome To ",bank_private_details.bank_name)
        print("Please Choose Your Own Atm Id,With 10 Numbers")
        atm_number=input("Atm Id:")
        if len(atm_number)==10:
            print("Your Atm Id is:",atm_number)
        else:
            print("Please Enter 10 Digits For Atm Id!")
    
    @property
    def user_atm_pass(self):
        return self.__atm_pass
    
    @user_atm_pass.setter
    def user_atm_pass(self):
        print("Welcome To ",bank_private_details.bank_name)
        print("Please Choose Your Own Atm Password,With 6 Digits")
        atm_pass=input("Atm Pass:")
        if len(atm_pass)==6:
            print("Your Atm Pass Successfully Changed")
        else:
            print("Please Enter 6 Digits For Atm Pass!")
    
    @property
    def user_atm_cvv(self):
        return self.__atm_cvv
    
    @property
    def withdrawal_amount(self):
        return self.account_bank.account_balance_update_add
    
    @withdrawal_amount.setter
    def withdrawal_amount(self):
        money=int(input("Enter Your Amount:"))

        if self.account_bank.deduct_balance(money):
            print(money,"Succesfully Withdrawn")
        else:
            print('Insufficient Balance')

    @property
    def add_amount(self):
        return self.account_bank.account_balance_update_add
    
    @add_amount.setter
    def add_amount(self):
        money=int(input("Enter Your Amount:"))

        self.account_bank.add_balance(money)
        print(money,"Succesfully Added")

#DAY 25(Practice)

bank_data=bank_private_details()

print("Welcome Sir To Our Bank",bank_data.bank_name,"\nWe Ensure The Quality Of Experience For Our User...\n\n") 

while True:

    print("Do You Want To See Other Information About US?\n" \
    "1.Yes\n" \
    "2.No")
    user_choice=input(":")
    if user_choice.lower()!="yes":
        print("Thank You For Giving Your Valueable Time")
        break
    else:
        print("Choose The Number Which You Want To See:\n" \
        "1.Bank Id\n" \
        "2.Bank No Of Branches\n" \
        "3.Bank Headquarter\n" \
        "4.Bank Sub Headquarter\n" \
        "5.Bank Finance Hub\n" \
        "6.Bank Contact No")
        user_bank_choice1=int(input("You Want To See:--"))

        if user_bank_choice1==1:
            print("Our Bank Id Is:",bank_data.bank_id)
        elif user_bank_choice1==2:
            print("Our Bank Number Of Branches Have:--",bank_data.bank_branches)
        elif user_bank_choice1==3:
            print("Our Bank Headquarter Situated In:--",bank_data.bank_headquarter)
        elif user_bank_choice1==4:
            print("Our Bank's Sub Headquarter Situated In:--",bank_data.bank_sub_hq1)
        elif user_bank_choice1==5:
            print("Our Bank's Finance Hub Situated In:--",bank_data.bank_finance_region)
        elif user_bank_choice1==6:
            print("Our Bank's Contact Number :--",bank_data.bank_contact_no)
        else :
            print("Invalid Number Please Choose Between 1-6 !!!")

print("For Becoming The Customer Of Our Bank , Please Fill Up The Form...")

while True:
    user_value=input("Choose Your Own Bank Account No:")
    if len(user_value)==10 and user_value.isdigit():
        break
    else:
        print("10 Digit Required! Or Numbers Only")

while True:
    user_value_name=input("Provide Your Name:")
    if user_value_name.replace(" ","").isalpha():
        break
    else:
        print("No Special Characters Allowed!")

while True:
    user_value_pass=input("Provide Password:")
    if len(user_value_pass)>=6:
        break
    else:
        print("Minimum 6 Digits Password Required!")

while True:
    user_value_age=int(input("Your Age:"))
    if 16<=user_value_age<=120:
        break
    else:
        print("Please Use Right Age!")

while True:
    user_value_gender=input("Sex:\tMale\tFemale\tOthers\t:")
    if user_value_gender.lower()=="male" or user_value_gender.lower()=="female" or user_value_gender.lower()=="others":
        break
    else:
        print("Either Male Or Female Or Others!")

while True:
    user_father_name=input("Provide Your Father's Name:")
    if user_father_name.replace(" ","").isalpha():
        break
    else:
        print("No Special Characters Allowed!")

while True:
    user_mother_name=input("Provide Your Mother's Name:")
    if user_mother_name.replace(" ","").isalpha():
        break
    else:
        print("No Special Characters Allowed!")

while True:
    user_acc_id=input("Create Your Own Bank Account Id:")
    if len(user_acc_id)==5:
        break
    else:
        print("5 Digit Required!")

while True:
    user_phone_number=input("Give Your Phone Number:")
    if len(user_phone_number)==10 and user_phone_number.isdigit():
        break
    else:
        print("10 Digit Required! Or Numbers Only")

while True:
    user_branch=input("Bank Branch Name:")
    if user_branch.isalpha():
        break
    else:
        print("Branch Name Only In Single Word")

while True:
    user_area=input("Your Area(City/Town/Village):")
    if user_area.replace(" ","").isalpha():
        break
    else:
        print("Provide Your Area")

while True:
    user_pin_code=input("Your Pin Code:")
    if len(user_pin_code)==6 and user_pin_code.isdigit():
        break
    else:
        print("Please Provide Your Pin  Code")

while True:
    user_balance=input("Add Amount In Your Bank Account:")
    if user_balance.isdigit() or user_balance.isdecimal():
        break
    else:
        print("Bruh Money Only Not Your Girlfriend's Name")

while True:
    user_email_address=input("Provide Your Email Address:")
    if user_email_address.endswith("@gmail.com"):
        break
    else:
        print("Provide Your Email Address and add @gmail.com")

while True:
    user_address=input("Give Your Address:")
    if user_address.strip()!="":
        break
    else:
        print("Provide Your Area")


user_data=bank_account_details_of_use(
    user_value,
    user_value_name,
    user_value_pass,
    user_father_name,
    user_mother_name,
    user_acc_id,
    user_phone_number,
    user_branch,
    user_area,
    user_pin_code,
    int(user_balance),
    user_email_address,
    user_address,
    user_value_age,
    user_value_gender
)

while True:
    print("Do You Want To Change Any Details Of Your Bank Account?\n")
    choice_yes_no=input("Yes or No:")
    if choice_yes_no.lower()=="yes":
        print("Choose Option->\n" \
        "1.Bank Account Password\n" \
        "2.Bank Account Phone Number\n" \
        "3.Bank Account Name\n" \
        "4.Bank Account Father Name\n" \
        "5.Bank Account Mother Name\n" \
        "6.Bank Account Email Id\n" \
        "7.Bank Account Address\n" \
        "8.Others\n" \
        "9.Exit\n")
        user_option_selection=int(input("Option:"))
        if user_option_selection==1 or user_option_selection==2:
           user_data.user_account_pass_phno_reset()
        elif user_option_selection==3:
            user_data.account_data_name()
        elif user_option_selection==4:
            user_data.account_father_name()
        elif user_option_selection==5:
            user_data.account_mother_name()
        elif user_option_selection==6:
            user_data.account_email_id()
        elif user_option_selection==7:
            user_data.account_address_details()
        elif user_option_selection==8:
            print("Choose Option->\n" \
            "1.For Seeing Pass or Phone Number\n" \
            "2.For Balance Update \n" \
            "3.For Transaction History\n" \
            "4.For Adding Money\n" \
            "5.For Deduct Balance\n" \
            "6.Exit\n")

            user_other=int(input(":"))
            if user_other==1:
                user_data.user_accno_pass_show()
            elif user_other==2:
                user_data.account_balance_update_add()
            elif user_other==3:
                user_data.user_transaction_history()
            elif user_other==4:
                user_data.add_balance()
            elif user_other==5:
                user_data.deduct_balance()
            elif user_data==6:
                break
            else:
                print("Invalid Input")
        elif user_option_selection==9:
            break
        else:
            print("Invalid Input Choose Correct Option")
    break
    
#DAY 26(PRACTICE)
#DAY 27(PRACTICE)
#DAY 28(PRACTICE)
#DAY 29(PRACTICE)-[Git & Github]

print("Thanks For Submitting Bank Details...\n\n")
print("Do You Want To Use Atm Service?...\n" \
"Press 1 for Yes\t \t Press 2 for No")

while True:
    user_input_1=int(input(":"))
    if user_input_1==1:
        user_atm_form=atm_registration_form(user_data)
        user_atm_form.user_atm_application_form()
        break
    else:
        print("Thank You Seeing You Again...")
        break
while True:
    Atm_Id=input("Choose Numbers For Your Own Atm Id(6):")
    if len(Atm_Id)==6 and Atm_Id.isdigit():
        break
    else:
        print("Please Select 6 Digits and No Characters!")
while True:
    Atm_Number=input("Choose Numbers For Your Atm Card(10):")
    if len(Atm_Number)==10 and Atm_Number.isdigit():
        break
    else:
        print("Please Choose 10 digits for your atm number and no characters!")
while True:
    Atm_Pass=input("Choose Your Atm Password(4):")
    if len(Atm_Pass)==4 and Atm_Pass.isdigit():
        break
    else:
        print("Please Choose 4 digits for your Atm Pass and No Characters!")
while True:
    Atm_Cvv=input("Choose Your Atm Cvv(3):")
    if len(Atm_Cvv)==3 and Atm_Cvv.isdigit():
        break
    else:
        print("Please Choose 3 digits for your Atm Cvv and no characters!")
while True:
    Atm_user_name=input("Enter Your Name:").strip()
    if Atm_user_name.count(" ")==1 and all(c.isalpha() or c==" " for c in Atm_user_name) and Atm_user_name==Atm_user_name.upper():
        break
    else:
        print("Only In Capital Letters + No Special Characters Are Allowed!")
while True:
    Atm_ph_Number=input("Give Phone Number For Your Atm(10):")
    if len(Atm_ph_Number)==10 and Atm_ph_Number.isdigit():
        break
    else:
        print("Please Choose 10 digits for your Phone number and no characters!")
while True:
    year=random.randint(2026,2040)
    month=random.randint(1,12)
    day=random.randint(1,calendar.monthrange(year,month)[1])
    random_date=datetime.date(year,month,day)
    Atm_DateTime=random_date.strftime("%d/%m/%Y")
    print("Timeline of Card:",Atm_DateTime)
    break
while True:
    card_type=["Visa","MaasterCard","Rupay"]
    Atm_card=random.choice(card_type)
    print("Your Atm Card Type Is:",Atm_card)
    break
user_atm=atm_details_account_of_user(user_data,Atm_Id,Atm_Number,Atm_Pass,Atm_Cvv,Atm_user_name,Atm_ph_Number,Atm_DateTime,Atm_card)
while True:
    print("Welcome To Our Atm Facility:\n" \
    "Choose An Option For Further Operations->\n" \
    "1.Withdrawal\n" \
    "2.Deposit\n" \
    "3.Exit\n")
    user_atm_money=input(":")
    if user_atm_money=='1':
        money=int(input("Enter Amount To Withdraw:"))
        if user_atm.account_bank.deduct_balance(money):
            print(f"{money}Successfully Withdrawn")
        else:
            print("Insufficient Balance")
    elif user_atm_money=='2':
        money=int(input("Enter Amount to Deposit:"))
        user_atm.account_bank.add_balance(money)
        print(f"{money}successfully deposited")
    elif user_atm_money=='3':
        print("Thanks For Using Our Facility..")
        break
    else:
        print("invalid input")
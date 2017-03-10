# coding=utf-8
from django.shortcuts import get_object_or_404

from bank.models import Personal_Information
from loan.models import Loan, Expenses


########################################################################################################################

# credit scoring system function will be written here
# Analyzes loan worthiness and limits amount available to be borrowed

########################################################################################################################
class Account(object):
    def __init__(self, acc_no):
        self.account_no = acc_no
        # an account number has to belong to a person
        self.holder = get_object_or_404(Personal_Information, pk=acc_no)
        # an account has the following
        self.current = None
        self.saving = None
        self.loan = None
        self.atm = None
        self.registrationdate = None
        self.creditscore = None

        # am not sure if the below functions are required

    def personal_detail(self, *args, **kwargs):
        self.registrationdate = self.holder.date_registered
        return self.registrationdate

    def personloan(self):
        self.loan = self.holder.loan_ac
        return self.loan

    def personsaving(self):
        self.saving = self.holder.saving_ac
        return self.saving

    def personcurrent(self):
        self.current = self.holder.current_ac
        return self.current


# Objects inheriting from Class Account

class Current(Account):
    def __init__(self, acc_no, amount, reg_date):
        # applies the same mro as the parent
        super(Current, self).__init__(acc_no)
        # other items that make up the current account
        self.amount = amount
        self.reg_date = reg_date
        # a current accounts may be registered with an ATM
        self.atm = None

        # ToAdd functions for evaluating credit score

        def balance(*args, **kwargs):
            if self.amount < 0:
                score = -1
            elif self.amount < self.saving:
                score = -0.5
            elif self.amount == self.saving:
                score = 0
            elif self.amount > self.saving:
                score = 0.5
            return score

        def loanCompbalance(*args, **kwargs):
            if self.amount < self.loan.loan_amount:
                score = -1
            elif self.amount == self.loan.loan_amount:
                score = 0
            elif self.amount > self.loan.loan_amount:
                score = 1

                # To find out, how does having an ATM affect one credibily
                # Tasked Shem to define how active the account has been, suggest this be defined at account level


class Saving(Account):
    def __init__(self, acc_no, amount, reg_date):
        # applies the same mro as the parent
        super(Saving, self).__init__(acc_no)
        # other items that make up the current account
        self.amount = amount
        self.reg_date = reg_date

    # The savings has to exist for a person tobe given  a loan
    def savingexist(self):
        if self.saving:
            return 0
            # Other rules like the minimu amount deposited etc.

            # Tasked Shem to define how active the account has been, suggest this be defined at account level

            # ToAdd functions for evaluating credit score


class Atm(Current):
    def __init__(self, number, expiry, attached):
        self.atm = attached
        self.number = number
        self.expity = expiry

        # ToAdd functions for evaluating credit score

    #
    # class Loan(Account):
    #     # this class will super alot from other class functions+
    #     def __init__(self, acc_no, type, amount):
    # super(Loan, self).__init__(acc_no)
    # self.type = type
    # self.amount = amount
    # self.loanee = None
    # self.status = None
        # def status(self, *args, **kwargs):


class Address(object):
    def __init__(self, email, phoneno):
        self.email = email
        self.pnoneno = phoneno
        # Other fields
        self.postal = None
        self.physical = None


class Postal(Address):
    def __init__(self, postal):
        self.postal = postal


class Residency(Address):
    def __init__(self, town, estate):
        self.estate = estate
        self.town = town
        # other fields
        self.houseno = None


class Loanee(Loan):  # Focus on this class
    def __init__(self, new, amount, participating):
        self.new_customer = new
        self.loan_amount = amount
        # other variables
        self.loan_type = None  # Different loan types have different conditions
        self.loan_period = None
        self.loan_status = None  # check will be both for new existing and returning, checks the state of their previous loans
        self.loan_purpose = None  # Belongs to Judgemental
        self.participanting = participating
        self.criminal_offence = None
        self.defaults_payments = None
        self.bankruptcy = None
        self.child_support = None
        # connected fields
        self.expenses = None
        self.economy = None
        if self.participanting is not "Only me":
            self.participant_details = None
            self.participant_no = None

    # Have to ensure these values are in existence before calling the function, otherwise these funtions are useless
    def selfcheckBank(self):
        if self.bankruptcy:
            score = -1
        else:
            score = 0
        return score

    def selfchackCriminal(self):
        if self.criminal_offence:
            score = -1
        else:
            score = 0
        return score  # accompanying documents may be needed as prof, or even physical visit of th eite

    def selfcheckChild(self):
        if self.child_support:
            score = 0
        else:
            score = 1
        return score

    def selfcheckExtreme(self):
        if self.criminal_offence and self.bankruptcy:
            score = -3
        elif self.criminal_offence and self.child_support:
            score = -2
        elif self.child_support and self.bankruptcy:
            score = -2
        elif self.bankruptcy and self.child_support and self.criminal_offence:  # extreme case!
            score = -4
        return score

    # to check the purposes, we shall create a dictionary of keywords to look for
    def checkpurpose(self):
        if self.loan_purpose != "":
            string_pupose = self.loan_purpose
            # perform operations on that string
            return self.loan_purpose

    # function for splitting the purpose into single words
    def splitpurpose(self):
        purpose_list = self.checkpurpose().split(" ")
        return purpose_list

    # function for reading a predefine dictionary with key words needed to for decision making
    def read_dict(self, filename):
        data = open(filename, 'r')
        temp = []
        for line in data:
            temp.append(line.strip('\n'))
        data.close()
        return temp

    # function to campare the purpose defined and the values in the distionary
    def compdata(self, words):
        match = []
        for word in words:
            if word in self.splitpurpose():
                match.append(word)
        return match

    # define a function to evaluate the severity of the words found
    def evaluatewords(self):
        dictionary = self.read_dict('key_words')
        match_words = self.compdata(dictionary)
        # checks
        for word in match_words:
            if (word).lower() in ['land', 'vehicle', 'funeral', 'marriage', 'vacation', 'debt']:
                score = -2
            else:
                score = 0
        return score


class Guarantor(object):
    def __init__(self, fname, sname, idno, pin):
        self.firtname = fname
        self.surname = sname
        self.id = idno
        self.pin = pin
        # other fields, though not mandatory
        self.passport = None
        self.address = None


class OtherGuarantor(Guarantor):
    def __init__(self, fname, sname, idno, pin):
        super(OtherGuarantor, self).__init__(fname, sname, idno, pin)


class Expenses(Expenses):
    def __init__(self, rent, elec, water, enter, school):
        self.rent = rent
        self.electricity = elec
        self.water = water
        self.entertainment = enter
        self.school_fees = school
        self.others = None




# Sample function of how the code is supposedly going to function
# polycarp = Account(11840)
# check if Polycarp has registered a current account
# Logic is that Having an account does not imply having current account
# We register a current account and if the same a/c number matches the a/c no for polycarp it's assigned to him
# p_current.current = Current(11840, 5000, 09/03/2017)   #Also from this object it's where we shall get checks related
# A person can have more than one current/savings/loans account

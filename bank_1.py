class Account:
    def __init__ (self,accnumber,balance):
        self.accnumber=accnumber
        self.balance=balance
class SBAccount(Account):
    def __init__(Self,accnumber,balance):
        super().__init__(accnumber,balance)
    def deposit(self,amount):
        print("Current balance ",self.balance)
        self.balance+=amount
        print("New balance",self.balance)
    def withdraw(self,amount):
        if((self.balance-amount)>1000):
            print("Current balance ",self.balance)
            self.balance-=amount
            print("New balance ",self.balance)
    def calc_interest(self):
        print("Current balance ",self.balance)
        x= self.balance * 0.04
        self.balance += x
        print("New balance ",self.balance)
class FDAccount(Account):
    def __init__(self,accnumber,balance,period):
        super().__init__(accnumber,balance)
        self.period=period
    def calc_interest(self):
        return self.balance*0.825*self.period
    def close(self):
        print("Deposited amount",self.balance)
        self.balance += self.calc_interest()
        print("Maturity Amount:",self.balance)
class customer:
    sbaccnum=1001
    fdaccnum=2001
    def __init__(self,cust_id,name,address):
        self.cust_id=cust_id
        self_name=name
        self_address=address
        self.sb = self.fd = None
    def createaccount(self,type):
        if( type == 1 ):
            amt = float(input("Enter balance"))
            self.sb=SBAccount(customer.sbaccnum,amt)
            customer.sbaccnum += 1
        elif( type == 2 ):
            amt = float(input("Enter balance"))
            period=int(input("Enter num of years:"))
            self.fd = FDAccount(customer.fdaccnum,amt,period)
            customer.fdaccnum += 1
        else:
            print("Invalid Type")
    def transaction(self,type):
        if ( type == 1):
            amt = float(input("Enter amount:"))
            self.sb.deposit(amt)
        elif( type == 2 ):
            amt=float(input("Enter amount"))
            self.sb.withdraw(amt)
        elif( type == 3 ):
            self.sb.calc_interest()
        elif( type == 4):
            self.fd.close()
        else:
            print("Invalid type")
if __name__ == '__main__':
    c=[]
    i=0
    while True:
        print("SB Account   --1")
        print("FD Account   --2")
        print("Exit   --3")
        ch=int(input("Enter choice"))
        match(ch):
            case 1:
                print('New SB account ---1')
                print('Deposit        ---2')
                print('Withdraw       ---3')
                print('Calc interest  ---4')
                print('Exit           ---5')
                ch1=int(input("Enter choice"))
                match(ch1):
                    case 1:
                        name=input("Enter name:")
                        address=input("Enter address")
                        cu=customer(i,name,address)
                        c.append(cu)
                        c[i].createaccount(1)
                        i=i+1
                    case 2:
                        cid=int(input("Enter customer id:"))
                        c[cid].transaction(1)
                    case 3:
                        cid=int(input("Enter customer id:"))
                        c[cid].transaction(2)
                    case 4:
                        cid=int(input("Enter customer id:"))
                        c[cid].transaction(3)
                    case 5:
                        break
            case 2:
                print('New FD account ---1')
                print('close  ---2')
                print('Exit   ---3')
                ch1=int(input("Enter choice"))
                match(ch1):
                    case 1:
                        name=input("Enter name:")
                        address=input("Enter address")
                        cu=customer(i,name,address)
                        c.append(cu)
                        c[i].createaccount(2)
                        i=i+1
                    case 2:
                        cid=int(input("Enter customer id:"))
                        c[cid].transaction(4)
                    case 3:
                        break
        if ch == 3:
            break
                    
                    

                
                        
                        
             












            
            

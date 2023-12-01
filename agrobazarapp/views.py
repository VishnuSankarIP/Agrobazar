from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime 
from django.core.files.storage import FileSystemStorage
import MySQLdb
import webbrowser
db=MySQLdb.connect('localhost','root','','db_agrobazar')
c=db.cursor()
   ######################################################################
#                           SMS FUNCTION
######################################################################
 # def sendsms(ph,msge):
  #  sendToPhoneNumber= ph
   # url = "http://sms.mdsmedia.in/http-api.php?username=7000183&password=LCCCOK123&senderid=LCCCOK&route=23&number="+str(sendToPhoneNumber)+"&message="+str(msge)
 #    contents = urllib.request.urlopen(url)
  #  webbrowser.open(url)
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
def farmerreg(request):
    msg=""
    m=""
    if(request.POST):
        name=request.POST.get("name")
        address=request.POST.get("address")
        city=request.POST.get("city")
        district=request.POST.get("district")
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        phone=request.POST.get("phone")
        email=request.POST.get("email") 
        password=request.POST.get("password")
        
        m="select count(*) count from tbl_farmerreg where email='"+str(email)+"'"
        c.execute(m)  
        msg="Already Registered"
        i=c.fetchone()
        if(i[0]==0):
            m="insert into tbl_farmerreg(name,address,city,district,gender,dob,phone,email,password,status) values('"+str(name)+"','"+str(address)+"','"+str(city)+"','"+str(district)+"','"+str(gender)+"','"+str(dob)+"','"+str(phone)+"','"+str(email)+"','"+str(password)+"','0')"
            c.execute(m)
            db.commit()
            s="insert into tbl_login(username,password,usertype) values('"+str(email)+"','"+str(password)+"','farmer')"
            c.execute(s)
            msg="Regitration Successfull"
            db.commit()
    return render(request,"farmerreg.html",{"msg":msg})
def farmerregshow(request):
    c.execute("select * from tbl_farmerreg where status='0'")
    j=c.fetchall() 
    data=selectfarmer()
    print(j)
    return render(request,"farmerregshow.html",{"j":j,"data":data})
def selectfarmer():
    data=""
    c.execute("select * from tbl_farmerreg where status='1'")
    data=c.fetchall()
    return data
def approvefarmer(request):
    msg=""
    msge=""
    id=request.GET.get("id")
    s="update tbl_farmerreg set status='1' where id='"+str(id)+"'"
    c.execute(s)
    msg="Approved......."
    db.commit()
    m="select phone from tbl_farmerreg where id='"+str(id)+"'"
    c.execute(m)
    d=c.fetchone()
    contact=d[0]
    msge="Your Agrobazar registeration is approved"
    return HttpResponseRedirect("/farmerregshow")
  #  sendsms(contact,msge)
    # c.execute("select utype from tbl_login where ='"+email+"'")
    # k=c.fetchone()
    # if(k[0]=='farmer'):
    #     n="select phone from tbl_farmerreg where email='"+email+"'"
    #     c.execute(n)
    #     d=c.fetchone()
    #     contact=d[0]
    #     msg="Your registeration is approved"
    #     sendsms(contact,msg)
    return render(request,"farmerregshow.html",{"msg":msg })
def deletefarmer(request):
    msg=""
    id=request.GET.get("id")
    s="update tbl_farmerreg set status='3' where id='"+str(id)+"'"
    c.execute(s)
    msg="Deleted......."
    db.commit()
    return render(request,"farmerregshow.html",{"msg":msg})
def deliveryboyreg(request):

    msg=""
    m=""
    if(request.POST):
        name=request.POST.get("name")
        address=request.POST.get("address")
        city=request.POST.get("city")
        district=request.POST.get("district")
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        phone=request.POST.get("phone")
        email=request.POST.get("email") 
        password=request.POST.get("password")
        
        m="select count(*) count from tbl_deliveryboyreg where email='"+str(email)+"'"
        c.execute(m)  
        msg="Already Registered"
        i=c.fetchone()
        if(i[0]==0):
            m="insert into tbl_deliveryboyreg(name,address,city,district,gender,dob,phone,email,password,status) values('"+str(name)+"','"+str(address)+"','"+str(city)+"','"+str(district)+"','"+str(gender)+"','"+str(dob)+"','"+str(phone)+"','"+str(email)+"','"+str(password)+"','1')"
            c.execute(m)
            db.commit()
            s="insert into tbl_login(username,password,usertype) values('"+str(email)+"','"+str(password)+"','deliveryboy')"
            c.execute(s)
            msg="Regitration Successfull"
            db.commit()
    return render(request,"deliveryboyreg.html",{"msg":msg})
def deliveryboyregshow(request):
    c.execute("select * from tbl_deliveryboyreg where status='1'")
    j=c.fetchall() 
    print(j)
    data=selectcustomer()
    return render(request,"deliveryboyregshow.html",{"j":j,"data":data})    

def customerreg(request):

    msg=""
    m=""
    if(request.POST):
        name=request.POST.get("name")
        address=request.POST.get("address")
        city=request.POST.get("city")
        district=request.POST.get("district")
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        phone=request.POST.get("phone")
        email=request.POST.get("email") 
        password=request.POST.get("password")
        
        m="select count(*) count from tbl_customerreg where email='"+str(email)+"'"
        c.execute(m)  
        msg="Already Registered"
        i=c.fetchone()
        if(i[0]==0):
            m="insert into tbl_customerreg(name,address,city,district,gender,dob,phone,email,password,status) values('"+str(name)+"','"+str(address)+"','"+str(city)+"','"+str(district)+"','"+str(gender)+"','"+str(dob)+"','"+str(phone)+"','"+str(email)+"','"+str(password)+"','0')"
            c.execute(m)
            db.commit()
            s="insert into tbl_login(username,password,usertype) values('"+str(email)+"','"+str(password)+"','customer')"
            c.execute(s)
            msg="Regitration Successfull"
            db.commit()
    return render(request,"customerreg.html",{"msg":msg})
def customerregshow(request):
    c.execute("select * from tbl_customerreg where status='0'")
    j=c.fetchall() 
    print(j)
    data=selectcustomer()
    return render(request,"customerregshow.html",{"j":j,"data":data})    
def login(request):
    msg=""
    if(request.POST):
        email=request.POST.get("email")
        password=request.POST.get("password")
        s="select count(*) from tbl_login where username='"+str(email)+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]==0):
            msg="User doesnt exist"
        else:
            s="select * from tbl_login where username='"+str(email)+"' and password='"+str(password)+"'"
            c.execute(s)
            y=c.fetchone()
            request.session['id']=y[0]
             
            if y[3]=='admin':
                msg="Welcome Administrator..........."
                return HttpResponseRedirect("/adminhome")
            elif y[3]=='farmer':
                s="select * from tbl_farmerreg where email='"+str(email)+"' "
                
                c.execute(s)
                y=c.fetchone()
                request.session['id']=y[0]

                return HttpResponseRedirect("/farmerhome")
            elif y[3]=='customer':
                s="select * from tbl_customerreg where email='"+str(email)+"'"
                
                c.execute(s)
                y=c.fetchone()
                request.session['id']=y[0]
                return HttpResponseRedirect("/customerhome")
            elif y[3]=='deliveryboy':
                s="select * from tbl_deliveryboyreg where email='"+str(email)+"'"
                
                c.execute(s)
                y=c.fetchone()
                request.session['id']=y[0]
                return HttpResponseRedirect("/deliveryboyhome")
            
    return render(request,"login.html",{"msg":msg})
def adminhome(request):
    return render(request,"adminhome.html")
def farmerhome(request):
    return render(request,"farmerhome.html")
def deliveryboyhome(request):
    return render(request,"deliveryboyhome.html")
def customerhome(request):
    return render(request,"customerhome.html")

def approvedeliveryboy(request):
    msg=""
    msge=""
    id=request.GET.get("id")
    s="update tbl_deliveryboyreg set status='1' where id='"+str(id)+"'"
    c.execute(s)
    msg="Approved......."
    db.commit()
    m="select phone from tbl_deliveryboyreg"
    c.execute(m)
    d=c.fetchone()
    contact=d[0]
    msge="Your registeration is approved"
   # sendsms(contact,msge)
    
    return render(request,"deliveryboyregshow.html",{"msg":msg })
def approvecustomer(request):
    msg=""
    msge=""
    id=request.GET.get("id")
    s="update tbl_customerreg set status='1' where id='"+str(id)+"'"
    c.execute(s)
    msg="Approved......."
    db.commit()
    data=selectcustomer()
    m="select phone from tbl_customerreg where id='"+str(id)+"'"
    c.execute(m)
    d=c.fetchone()
    contact=d[0]
    msge="Your Agrobazar registeration is approved"
    # sendsms(contact,msge)
    return HttpResponseRedirect("/customerregshow")
    return render(request,"customerregshow.html",{"msg":msg,"data":data})

def deletedeliveryboy(request):
    msg=""
    id=request.GET.get("id")
    s="update tbl_deliveryboyreg set status='3' where id='"+str(id)+"'"
    c.execute(s)
    msg="Deleted......."
    db.commit()
    return render(request,"deliveryboyregshow.html",{"msg":msg})
def deletecustomer(request):
    msg=""
    id=request.GET.get("id")
    s="update tbl_customerreg set status='3' where id='"+str(id)+"'"
    c.execute(s)
    msg="Deleted......."
    db.commit()
    return render(request,"customerregshow.html",{"msg":msg})


def selectdeliveryboy():
    data=""
    c.execute("select * from tbl_deliveryboyreg where status='1'")
    data=c.fetchall()
    return data
def selectcustomer():
    data=""
    c.execute("select * from tbl_customerreg where status='1'")
    data=c.fetchall()
    return data

def addproduct(request):
    msg=""
    m=""
    data=""
    farmerid=request.session['id']
    if(request.POST):
        
        name=request.POST.get("name")
        category=request.POST.get("category")
        description=request.POST.get("description")
        price=request.POST.get("price")
        
        image=request.FILES["image"]
        fs=FileSystemStorage()
        filename=fs.save(image.name,image)
        uploaded_file_url=fs.url(filename)
        m="insert into tbl_addproduct(farmerid,productname,category,description,price,image,status) values('"+str(farmerid)+"','"+str(name)+"','"+str(category)+"','"+str(description)+"','"+str(price)+"','"+uploaded_file_url+"','1')"
        c.execute(m)
        db.commit()
        msg="Added......."
    data=viewaddproduct(farmerid)
    return render(request,"productadd.html",{"msg":msg,"data":data})
def viewaddproduct(fid):
    farmerid=fid
    data=""
    c.execute("select * from tbl_addproduct,tbl_farmerreg where tbl_addproduct.status='1' and tbl_addproduct.farmerid='"+str(farmerid)+"' and tbl_addproduct.farmerid=tbl_farmerreg.id")
    data=c.fetchall()
    return data
def adminviewaddproduct(request):
    c.execute("select tbl_farmerreg.id,tbl_farmerreg.name,tbl_farmerreg.district,tbl_addproduct.productid,tbl_addproduct.productname,tbl_addproduct.category,tbl_addproduct.price,tbl_addproduct.image from tbl_farmerreg,tbl_addproduct where tbl_farmerreg.id=tbl_addproduct.farmerid and tbl_addproduct.status='1'")
    j=c.fetchall() 
    
    print(j)
    return render(request,"adminviewaddproduct.html",{"j":j})
def customerviewproduct(request):
    c.execute("select tbl_farmerreg.id as farmid, tbl_addproduct.productid, tbl_addproduct.productname, tbl_addproduct.category, tbl_addproduct.price, tbl_addproduct.image,tbl_farmerreg.name,tbl_addproduct.description from tbl_farmerreg, tbl_addproduct WHERE tbl_addproduct.status = '1' and tbl_farmerreg.id = tbl_addproduct.farmerid")
    j=c.fetchall() 
    
    print(j)
    return render(request,"customerviewproduct.html",{"j":j})
    
def deleteproduct(request):
    msg=""
    productid=request.GET.get("productid")
    c.execute("update tbl_addproduct set status='0' where productid='"+str(productid)+"'")
    msg="Deleted"
    db.commit()
    return render(request,"productadd.html")
    
def feedback(request):
    msg=""
    m=""
    
    if(request.POST):
        msg=""
        customerid=request.session['id']
        cartid=request.POST.get("cartid")
        title=request.POST.get("title")
        description=request.POST.get("description")
        today=datetime.today()
        
        m="insert into tbl_feedback(customerid,title,description,date,status,cartid) values('"+str(customerid)+"','"+str(title)+"','"+str(description)+"','"+str(today)+"','0','"+str(cartid)+"')"
        c.execute(m)
       
        db.commit()
        msg="Thank You..."

            
    return render(request,"feedback.html",{"msg":msg})
def viewfeedback(request):
    c.execute("select tbl_customerreg.name,tbl_feedback.title,tbl_feedback.description,tbl_feedback.date,tbl_feedback.cartid,tbl_cart.id from tbl_customerreg,tbl_feedback,tbl_cart where tbl_customerreg.id=tbl_feedback.customerid and tbl_cart.customerid=tbl_customerreg.id and tbl_cart.id=tbl_feedback.cartid ")
    j=c.fetchall() 
    data=selectfeedback()
    print(j)
    return render(request,"viewfeedback.html",{"j":j,"data":data})
def selectfeedback():
    data=""
    c.execute("select * from tbl_feedback where status='1'")
    data=c.fetchall()
    return data
def insertintocart(request):
    msg=""
    m=""
    if(request.POST):
        custid=request.session['id']
        
        farmerid=request.GET.get("farmerid")
        productid=request.GET.get("productid")
        price=request.GET.get("price")
        quantity=request.POST.get("quantity")
        bdate=datetime.today()
        rdate=request.POST.get("rdate")
        totalprice=int(price)*int(quantity)
        
        m="insert into tbl_cart(customerid,farmerid,productid,quantity,price,totalprice,bdate,rdate,status) values('"+str(custid)+"','"+str(farmerid)+"','"+str(productid)+"','"+str(quantity)+"','"+str(price)+"','"+str(totalprice)+"','"+str(bdate)+"','"+str(rdate)+"','ordered')"
        c.execute(m)
        msg="Added into cart......"
        db.commit()
    
         
    return render(request,"order.html",{"msg":msg,})
def viewcartproduct(request):
    farmerid=request.session['id']
    j=" "
    c.execute("select tbl_cart.id,tbl_cart.customerid,tbl_addproduct.productname,tbl_cart.quantity,tbl_cart.bdate,tbl_cart.rdate,tbl_cart.totalprice from tbl_cart,tbl_addproduct,tbl_farmerreg where tbl_addproduct.productid=tbl_cart.productid and tbl_cart.farmerid=tbl_farmerreg.id and tbl_cart.farmerid='"+str(farmerid)+"' and tbl_cart.status='ordered'")

    j=c.fetchall() 
    print(j)
    data=selectorder()
    
    return render(request,"viewcart.html",{"j":j,"data":data})
def cancelorder(request):
    cusid=request.GET.get("customerid")
    cartid=request.GET.get("cartid")
    c.execute("update tbl_cart set status='canceled' where id='"+str(cartid)+"' and customerid='"+str(cusid)+"'")
    db.commit()
    return render(request,"customerviewcart.html")

def customerviewcart(request):
    customerid=request.session['id']
    j=" "
    
    #c.execute("select tbl_cart.id,tbl_cart.customerid,tbl_addproduct.productname,tbl_cart.totalprice,tbl_cart.bdate,tbl_cart.rdate,tbl_cart.status,tbl_cart.farmerid,tbl_cart.productid from tbl_cart,tbl_addproduct,tbl_customerreg where tbl_addproduct.productid=tbl_cart.productid and tbl_cart.customerid=tbl_customerreg.id and tbl_cart.customerid='"+str(customerid)+"' and tbl_cart.status='delivered'")
    c.execute("select tbl_farmerreg.id as farmid, tbl_addproduct.productid, tbl_addproduct.productname, tbl_addproduct.category, tbl_addproduct.price, tbl_addproduct.image,tbl_cart.status,tbl_cart.id,tbl_cart.customerid,tbl_cart.totalprice,tbl_cart.bdate,tbl_cart.rdate,tbl_cart.quantity from tbl_farmerreg, tbl_addproduct,tbl_cart WHERE tbl_addproduct.status = '1' and tbl_farmerreg.id = tbl_addproduct.farmerid  and tbl_cart.productid=tbl_addproduct.productid and tbl_cart.customerid='"+str(customerid)+"'")
    j=c.fetchall() 
    
    print(j)
    return render(request,"customerviewcart.html",{"j":j})
def selectorder():
    data=""
    c.execute("select tbl_cart.id,tbl_cart.customerid,tbl_cart.productid,tbl_cart.quantity,tbl_cart.bdate,tbl_cart.rdate from tbl_cart,tbl_addproduct where tbl_addproduct.productid=tbl_cart.productid and tbl_cart.status='1'")
    data=c.fetchall()
    return data
def viewdeliveryboy(request):
    msg=""
    m=""
    if(request.POST):
        cartid=request.GET.get("cartid")
        custid=request.GET.get("customerid")
        did=request.POST.get("did")
        # m="select count(*) count from tbl_allocation where deliveryboyid='"+str(did)+"' and customerid='"+str(custid)+"'"
        # c.execute(m)  
        
        # msg=" Alrdy Allocated........."
        # i=c.fetchone()
        # if(i[0]==0):
        m="insert into tbl_allocation(deliveryboyid,customerid,cartid,status) values('"+str(did)+"','"+str(custid)+"','"+str(cartid)+"','Allocated')"
        c.execute(m)

        msg="Allocated"
        db.commit()
        c.execute("update tbl_cart set status='Approved' where tbl_cart.id='"+str(cartid)+"' and tbl_cart.customerid='"+str(custid)+"'")
        db.commit()
    data=selectdeliveryboy()

        
    return render(request,"deliveryboyregshow.html",{"data":data,"msg":msg}) 
def assigndeliveryboy(request):
    
    c.execute("update tbl_cart set status='delivered'  ")
    j=c.fetchall() 
    print(j)
    data=selectcustomer()
    return render(request,"deliveryboyregshow.html",{"j":j}) 

def selectassigndeliveryboy():
    data=""
    c.execute("select ")
    data=c.fetchall()
    return data

def deliveryboyvieworder(request):
    did=request.session['id']
    c.execute("select tbl_customerreg.id,tbl_farmerreg.name as farmername,tbl_customerreg.name as customername,tbl_customerreg.address,tbl_customerreg.city,tbl_customerreg.district,tbl_customerreg.phone,tbl_addproduct.productname,tbl_cart.totalprice,tbl_cart.id,tbl_allocation.status from tbl_farmerreg,tbl_customerreg,tbl_addproduct,tbl_deliveryboyreg,tbl_allocation,tbl_cart,payments where tbl_allocation.deliveryboyid='"+str(did)+"' and tbl_deliveryboyreg.id=tbl_allocation.deliveryboyid and tbl_allocation.status='Allocated' and tbl_cart.id=tbl_allocation.cartid and tbl_cart.farmerid=tbl_farmerreg.id and tbl_cart.customerid=tbl_customerreg.id and tbl_cart.productid=tbl_addproduct.productid and tbl_cart.id=tbl_allocation.cartid and tbl_allocation.customerid=tbl_customerreg.id and tbl_farmerreg.id=tbl_addproduct.farmerid and payments.cartid=tbl_cart.id and payments.customerid=tbl_customerreg.id and payments.productid=tbl_addproduct.productid")
    j=c.fetchall()
    print(j)
    return render(request,"deliveryboyvieworder.html",{"j":j})
   
def orderdelivered(request):
    msg=" "
    cartid=request.GET.get("cartid")
    #c.execute("update tbl_allocation set status='delivered' where tbl_allocation.cartid='"+str(cartid)+"' and tbl_allocation.cartid=tbl_cart.id")
    #c.execute("update tbl_allocation,tbl_cart set tbl_allocation.status='delivered' where tbl_allocation.cartid='"+str(cartid)+"' and tbl_allocation.cartid=tbl_cart.id")
    c.execute("SELECT tbl_customerreg.id, tbl_farmerreg.name AS farmername, tbl_customerreg.name AS customername, tbl_customerreg.address, tbl_customerreg.city, tbl_customerreg.district, tbl_customerreg.phone, tbl_addproduct.productname, tbl_cart.totalprice, tbl_cart.id, payments.status FROM tbl_farmerreg, tbl_customerreg, tbl_addproduct, tbl_deliveryboyreg, tbl_allocation, tbl_cart, payments WHERE tbl_deliveryboyreg.id = '8' AND tbl_deliveryboyreg.id = tbl_allocation.deliveryboyid AND tbl_allocation.status = 'Allocated' AND tbl_allocation.customerid = tbl_customerreg.id AND tbl_allocation.cartid = tbl_cart.id AND tbl_cart.customerid = payments.customerid AND tbl_cart.farmerid = tbl_addproduct.farmerid AND tbl_cart.productid = tbl_addproduct.productid AND payments.cartid = tbl_allocation.cartid AND tbl_addproduct.farmerid = tbl_farmerreg.id AND payments.cartid = tbl_cart.id AND payments.productid = tbl_addproduct.productid")
    db.commit
    
    c.execute("update tbl_allocation set status='delivered' where cartid='"+str(cartid)+"'")
    db.commit()
    c.execute("update tbl_cart set status='delivered' where id='"+str(cartid)+"'")
    db.commit()
    #now=datetime.now().time()
    now=datetime.now()
    c.execute("update tbl_allocation set deliverytime= '"+str(now)+"' where cartid='"+str(cartid)+"'")
    db.commit()
    msg="Done"
    return render(request,"deliveryboyvieworder.html",{"msg":msg})
def payment(request):
    msg=""
    cartid=request.GET.get("cartid")
    s="select totalprice from tbl_cart where id in(select id from tbl_cart where id='"+str(cartid)+"')"
    c.execute(s)
    i=c.fetchone()
    data=i[0]
    #a=customerviewcart({{i.3}})
    # return render(request,"payments.html",{"data":data})
    m="select count(*) count from payments where cartid='"+str(cartid)+"'"  
    c.execute(m)
    
    i=c.fetchone()
    if(i[0]>0):
        return HttpResponseRedirect("/customerviewcart")
    if(request.POST):
           
            cartid=request.GET.get("cartid")
            custid=request.GET.get("customerid")
            farmid=request.GET.get("farmerid")
            pdtid=request.GET.get("productid")
            cardno=request.POST.get("number")
            cvv=request.POST.get("security-code")
            namecard=request.POST.get("name")
            expiry=request.POST.get("expiration")
            tprice=request.POST.get("tprice")
            m="insert into payments(cartid,customerid,productid,cardnumber,cvv,nameoncard,expiration,price,status)values('"+str(cartid)+"','"+str(custid)+"','"+str(pdtid)+"','"+str(cardno)+"','"+str(cvv)+"','"+str(namecard)+"','"+str(expiry)+"','"+str(tprice)+"','paid')"
            c.execute(m)
            db.commit()
            msg="You have paid.You will get the product through Home Delivery"
            return HttpResponseRedirect("/customerviewcart")
    return render(request,"payments.html",{"msg":msg,"data":data})

def farmerviewpayments(request):
    fid=request.session['id']
    #c.execute("select payments.customerid,tbl_customerreg.name,tbl_addproduct.productname,payments.cardnumber,payments.cvv,payments.nameoncard,payments.expiration,payments.price from tbl_customerreg,tbl_addproduct,payments,tbl_farmerreg,tbl_cart where tbl_farmerreg.id='"+str(fid)+"' and payments.customerid=tbl_customerreg.id and tbl_addproduct.productid=payments.productid and tbl_cart.id=payments.cartid and tbl_cart.farmerid=tbl_farmerreg.id")
    #c.execute("select payments.customerid,tbl_customerreg.name,tbl_addproduct.productname,payments.cardnumber,payments.cvv,payments.nameoncard,payments.expiration,payments.price,tbl_allocation.status from tbl_customerreg,tbl_addproduct,payments,tbl_farmerreg,tbl_cart,tbl_allocation where tbl_farmerreg.id='"+str(fid)+"' and tbl_cart.id=payments.cartid and tbl_cart.farmerid=tbl_farmerreg.id and tbl_cart.productid=payments.productid and tbl_cart.customerid=payments.customerid and tbl_addproduct.productid=payments.productid and tbl_customerreg.id=payments.customerid ")
    c.execute("select payments.customerid,tbl_customerreg.name,tbl_addproduct.productname,payments.cardnumber,payments.cvv,payments.nameoncard,payments.expiration,payments.price,tbl_allocation.status from tbl_customerreg,tbl_addproduct,payments,tbl_farmerreg,tbl_cart,tbl_allocation where tbl_farmerreg.id='"+str(fid)+"' and tbl_cart.id=payments.cartid and tbl_cart.farmerid=tbl_farmerreg.id and tbl_cart.productid=payments.productid and tbl_cart.customerid=payments.customerid and tbl_addproduct.productid=payments.productid and tbl_customerreg.id=payments.customerid and tbl_allocation.cartid=payments.cartid and tbl_allocation.customerid=tbl_customerreg.id and tbl_allocation.cartid=tbl_cart.id")
    j=c.fetchall()
    print(j)

    return render(request,"farmerviewpayment.html",{"j":j})
def farmerviewdeliverystatus(request):
    fid=request.session['id']
    c.execute("select tbl_addproduct.productid,tbl_addproduct.productname,tbl_addproduct.category,tbl_addproduct.price,tbl_addproduct.image,tbl_allocation.status,tbl_allocation.deliverytime from tbl_addproduct,tbl_allocation,tbl_cart,tbl_farmerreg where tbl_addproduct.productid=tbl_cart.productid and tbl_cart.id=tbl_allocation.cartid and tbl_allocation.status='delivered' and tbl_farmerreg.id='"+str(fid)+"' and tbl_cart.farmerid=tbl_farmerreg.id")
    j=c.fetchall()
    print(j)
    return render(request,"farmerviewdeliverystatus.html",{"j":j})


    

def CustomerViewpdttDetails(request):
    
    
        
    
    # pid=Request.GET.get("id")
    msg=""
    m=""
    
    
    if(request.POST):
        farmerid=request.GET.get("farmerid")
        productid=request.GET.get("productid")
        price=request.GET.get("price")
        custid=request.session['id']
        s="select * from tbl_addproduct where productid = '"+str(productid)+"'"
        c.execute(s)
        data=c.fetchall()
        price = data[0][5]
        quantity=request.POST.get("quantity")
        bdate=datetime.today()
        rdate=request.POST.get("rdate")
        totalprice=int(price)*int(quantity)
        # c.execute("select qty from tbl_addproduct where pid = '"+str(pid)+"'")
        # q = c.fetchone()
        # cq = q[0]
        # if int(nqty) > cq:
        #     msg = "Invalid Stock"
        # else:
        # am = int(qty) * int(price)
        # c.execute("insert into cart (cid,pid,qty,price)values('"+str(cid)+"','"+str(pid)+"','"+str(qty)+"','"+str(am)+"')")
        # db.commit()
        # msg = "Order added successfully"
    # return render(Request,'CustomerViewProductDetails.html',{"data":data,"data1":data1,"msg":msg,"data2":data2,"data3":data3})
# Create your views here.

    
    # if(request.POST):
        
        
        
        m="insert into tbl_cart(customerid,farmerid,productid,quantity,price,totalprice,bdate,rdate,status) values('"+str(custid)+"','"+str(farmerid)+"','"+str(productid)+"','"+str(quantity)+"','"+str(price)+"','"+str(totalprice)+"','"+str(bdate)+"','"+str(rdate)+"','ordered')"
        c.execute(m)
        msg="Added into cart......"
        db.commit()
    
         
    return render(request,"order.html",{"msg":msg,})

def customerviewquick(request):
    productid=request.GET.get("productid")
    c.execute("select tbl_farmerreg.id as farmid, tbl_addproduct.productid, tbl_addproduct.productname, tbl_addproduct.category, tbl_addproduct.price, tbl_addproduct.image,tbl_farmerreg.name from tbl_farmerreg, tbl_addproduct WHERE tbl_addproduct.status = '1' and tbl_farmerreg.id = tbl_addproduct.farmerid and tbl_addproduct.productid='"+str(productid)+"'")
    j=c.fetchall() 
    
    print(j)

    return render(request,"customerviewquick.html",{"j":j})

def adminviewcart(request):
    c.execute("select * from tbl_cart")
    j=c.fetchall()
    print(j)
    return render(request,"adminviewcart.html",{"j":j})

def adminviewdeliveryboy(request):
    c.execute("select * from tbl_deliveryboyreg where status='1'" )
    data=c.fetchall()
    return render(request,"adminviewdeliveryboy.html",{"data":data})
def deletedboys(request):
    did=request.GET.get("did")
    c.execute("update tbl_deliveryboyreg set status='0' where id='"+str(did)+"'")
    db.commit()
    return HttpResponseRedirect('/adminviewdeliveryboy')
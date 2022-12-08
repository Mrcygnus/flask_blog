from flask import Flask, render_template, url_for, flash, redirect
app = Flask(__name__)
from forms import RegistrationForm,LoginForm

app.config['SECRET_KEY']='caa71c96d8678de41ec2624344f44d00'


posts = [
    {
        'author':'Corey Schafer',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'April 20,2018'
    },
    {
        'author':'Jane Doe',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted':'April 21,2018'
    }

]#for now just pretend we made a database call and got back this list of posts.We can pass this posts into our template just by 
#passing argument with our data




@app.route("/")#root page of our website..or home page
#Routes are what we type into our browser to go to different pages.In flask we do this usinng route decorators.Basically decoratores are
#to add additonal funtionality to existing functions.this app.route decorator will handle all of the complicated back end stuff
#and simply allow us to write a function that returns the information that will be shown on our website for this specific route
@app.route("/home")#two routes can be added to same function
def home():
    #return "Hello World!"   #this returns only plain text no any html included.
    #return "<h1>Home Page</h1>"#instead of returning html string we have to return template
    return render_template('home.html',posts=posts)
    #So whatever the variable name we use as argument name here  that we pass in ..and
    #you will have access to that variable in our template
    #templating engine that flask uses is Jinja2..it allows us to write our code in our templates


@app.route("/about")#another route
def about():
    #return "About Page"   #this returns only plain text no any html included.
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])#another route
def register():
    form = RegistrationForm()#we have created a instance of that form inside our application
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)
    
@app.route("/login",methods=['GET','POST'])#another route
def login():
    form = LoginForm()#we have created a instance of that form inside our application
    if form.validate_on_submit():
       if form.email.data == 'admin@blog.com' and form.password.data == 'password':
         flash('You have been logged in!','success')
         return redirect(url_for('home'))
       else :
        flash('Login Unsuccessful, Please check username and password','danger')
    return render_template('login.html',title='login',form=form)





if __name__ == '__main__':#no need to deal with environment variables you can run this script directly as python file
    app.run(debug=True)
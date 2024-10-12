from flask import Flask,redirect,url_for,render_template,session,flash,request
from forms import RegistrationForm, LoginForm, InputForm
from flask_bcrypt import Bcrypt
from database import User, db , TrackerInput
from model.model import prediction_cancer

app = Flask(__name__)

app.config['SECRET_KEY'] ='1234$'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)
bcrypt = Bcrypt(app)

# @app.before_request
# def check_auth():
#     block_route = ['/input','/predict','/result','/history']
#     if 'username'  not in session and request.path in block_route:
#         return redirect(url_for('login'))


def login_required(f):
    def wrap(*args, **kwargs):
        if 'username' not in session:
            flash('You need to login first!', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
    return wrap


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # hash
        hashed_password = bcrypt.generate_password_hash(password).decode('utf8')
        #create record 
        new_user = User(username=username, password=hashed_password)
        # add commit
        db.session.add(new_user)
        db.session.commit()
        flash('Register Successfull')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods = ['POST','GET'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_check = User.query.filter_by(username=username).first()
        if user_check and bcrypt.check_password_hash(user_check.password, password):
            session['username'] = username
            return redirect(url_for('input'))
    return render_template('login.html',form=form)

@app.route('/input')
@login_required
def input():
    form = InputForm()
    return render_template('input.html',form = form)



@app.route('/predict', methods=['POST','GET'])
@login_required
def predict():
    form = InputForm()
    if request.method == 'POST':
        mean_radius = form.mean_radius.data
        mean_perimeter = form.mean_perimeter.data
        mean_area = form.mean_area.data
        mean_concavity = form.mean_concavity.data
        mean_concave_points = form.mean_concave_points.data
        worst_radius =form.worst_radius.data
        worst_perimeter = form.worst_perimeter.data
        worst_area = form.worst_area.data
        worst_concavity = form.worst_concavity.data
        worst_concave_points = form.worst_concave_points.data

        features = [
            mean_radius,mean_perimeter,mean_area,mean_concavity,mean_concave_points,worst_radius,
            worst_perimeter,worst_area,worst_concavity,worst_concave_points
        ]

        predicted_class = prediction_cancer(features)
        username_login = session['username']
        user_check = User.query.filter_by(username =username_login ).first()
        new_input = TrackerInput(
            user_id= user_check.id,
            mean_radius = mean_radius,
            mean_perimeter = mean_perimeter ,
            mean_area = mean_area ,
            mean_concavity = mean_concavity,
            mean_concave_points = mean_concave_points,
            worst_radius = worst_radius ,
            worst_perimeter=  worst_perimeter,
            worst_area = worst_area ,
            worst_concavity = worst_concavity ,
            worst_concave_points = worst_concave_points,
            result = predicted_class
        )
        db.session.add(new_input)
        db.session.commit()


    return redirect(url_for('result' , predicted_class =predicted_class) )


@app.route('/result')
@login_required
def result():
    predicted_class = request.args.get('predicted_class')
    return render_template('result.html', predicted_class=predicted_class)


@app.route('/history')
@login_required
def history():
    if 'username' in session :
        username_login = session['username']
        user_check = User.query.filter_by(username =username_login ).first()
        inputs = TrackerInput.query.filter_by(user_id = user_check.id).all()
        return render_template('history.html',inputs = inputs)
    return redirect(url_for('login'))    

@app.route('/logout')
@login_required
def logout():
    session.pop('username')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
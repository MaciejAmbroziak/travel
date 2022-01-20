* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More detailed information about modules](#more-detailed-information-about-modules)
TBD
* [Application view](#application-view)
TBD

  
# General info
<details>
<summary>Click here to see general information about <b>Project</b>!</summary>
Travel allows to connect between users in order to travel</H2>
</details>

# Technologies
<details>
<summary>Click here to see used <b>technologies</b>!</summary>
<ul>
<li>Python 3.10</li>
<ol>
<li>Flask</li>
<li>SQLAlchemy</li>
<li>WTForm</li>
<li>bcrypt</li>
</ol>
<li>HTML</li>
<li>Postgres</li>
<li>Docker</li>
</ul>
</details>

# Setup
<p>You have to install <b>docker</b></p>
<p>You need to create .env file</p>
<p>In .env file you need to enter fields:</p>
<ul>
<li>POSTGRES_DB = "name of your db"</li>
<li>POSTGRES_USER = "your user name"</li>
<li>POSTGRES_PASSWORD = "your db password"</li>
<li>SQLALCHEMY_DATABASE_URI = "your db path" in format: postgresql+psycopg2://POSTGRES_USER:POSTGRES_PASSWORD@travel_db:5432/POSTGRES_DB</li>
</ul>
<p> Use command (in terminal):</p>
<li>docker-compose up --build</li>
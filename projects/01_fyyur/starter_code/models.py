lsfrom app import db

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.Column()
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column()
    image_link = db.Column(db.String(500))
    seeking_talent = db.Column()
    seeking_description = db.Column()
    facebook_link = db.Column(db.String(120))
    past_shows = db.Column()
    upcoming_shows = db.Column()
    # past_shows_count
    # upcoming_shows_count

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artists'

    artist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.Column()
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column()
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column()
    seeking_description = db.Column()
    upcoming_shows = db.Column()
    upcoming_shows_count = db.Column()
    past_shows = db.Column()
    past_shows_count = db.Column()


class Show(db.Model):
    __tablename__ = 'shows'
       
    venue_id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column()
    artist_id = db.Column()
    artist_name = db.Column()
    artist_image_link = db.Column()
    start_time = db.Column()


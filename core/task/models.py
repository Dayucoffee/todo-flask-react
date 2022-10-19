from .. import db

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))

	def __ref__(self):
		return '<Category {}>'.format(self.name)





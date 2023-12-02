function Particle(x, y, r, fixed) {

	let options = {
		friction: 0,
		restitution: 1,
		isStatic: fixed,
	}

	this.body = Bodies.circle(x, y, r, options);
	this.r = r;
	World.add(world, this.body);

	this.show = function() {
		let pos = this.body.position;
		let angle = this.body.angle;
		push();
		translate(pos.x, pos.y)
		rotate(angle);
		rectMode(CENTER);
		strokeWeight(1)
		stroke(255);
		fill(130);
		ellipse(0, 0, this.r * 2)
		pop(); 

	}

	this.isOffScreen = function() {
		let pos = this.body.position;
		return (pos.y > height + 100) 
	}

	this.removeFromWorld = function() {
		World.remove(world, this.body)
	}
}

function Boundary(x, y, w, h, a) {
	let options = {
		angle : a,
		isStatic: true
	}
	this.body = Bodies.rectangle(x, y , w , h, options);
	this.w = w;
	this.h = h;
	World.add(world, this.body);

	this.show = function() {
		let pos = this.body.position;
		let angle = this.body.angle;
		push();
		translate(pos.x, pos.y)
		rotate(angle);
		rectMode(CENTER);
		strokeWeight(1)
		stroke(255);
		fill("#b72c9e");
		rect(0, 0, this.w, this.h)
		pop(); 

	}
}

let Engine = Matter.Engine,
    World = Matter.World,
    Bodies = Matter.Bodies;
    Mouse = Matter.Mouse; 
    Constraint = Matter.Constraint
    MouseConstraint = Matter.MouseConstraint;

let engine;
let world; 
let boxes = [];
let boundaries = [];
let particles = [];
let mConstraint;



function setup() {
	let canvas = createCanvas(500, 500);
	canvas.parent('myContainer');
	engine = Engine.create();
	world = engine.world;
	Engine.run(engine);

	boundaries.push(new Boundary(250, height, width, 20, 0));
	let canvasmouse = Mouse.create(canvas.elt);
	let option = {
		mouse: canvasmouse,
	}

	mConstraint = MouseConstraint.create(engine, option)
	World.add(world, mConstraint);






	let prev = null;
	for (var i = 250; i < 460; i+=30) {
		
		let fixed = false;
		if (!prev) {
			fixed = true
		}
		P = new Particle(i, 100, 10, fixed); 
		//P2 = new Particle(200, 150, 10); 
		particles.push(P);
		// particles.push(P2);
		if (prev) {
			let options = {
				bodyA : P.body,
				bodyB: prev.body,
				length: 50,
				stiffness: 0.4
			}
			let constraint = Constraint.create(options);
			World.add(world, constraint);
		}
		prev = P;
	}
}







function draw() {
	background(51);
	for (let i = 0; i < particles.length; i++) {
		particles[i].show();
		if (particles[i].isOffScreen()) {
			particles[i].removeFromWorld();
			particles.splice(i, 1);
			i--;
		}
	}
	rectMode(CENTER)
	
	for (let i = 0; i < boundaries.length; i++) {
		boundaries[i].show();
	}

	if (mConstraint.body) {
		let pos = mConstraint.body.position
		let offset = mConstraint.constraint.pointB;
		fill(255, 0, 0)
		ellipse(pos.x, pos.y, 20, 20)
		stroke(255)
		line(pos.x + offset.x, pos.y + offset.y, mouseX, mouseY)
	}

	function toucheStarted() {
		if (mConstraint.body) {
			let pos = mConstraint.body.position
			let offset = mConstraint.constraint.pointB;
			fill(255, 0, 0)
			ellipse(pos.x, pos.y, 20, 20)
			stroke(255)
			line(pos.x + offset.x, pos.y + offset.y, mouseX, mouseY)
		}
	}

}















let path_socket = 'ws://'
        + window.location.host
        + '/ws/chat/room'
        + '/';

if (location.protocol === 'https:') {
    path_socket = 'wss://'
        + window.location.host
        + '/ws/chat/room'
        + '/';
}

const chatSocket = new WebSocket(path_socket);

function setup(){
	let myCanvas = createCanvas(400, 400);
	myCanvas.parent('myContainer');
	background(51);
}




function draw(){
	
}

function mouseDragged() {
	noStroke();
	ellipse(mouseX, mouseY, 20, 20);
	let data = JSON.stringify({
		x: mouseX,
		y: mouseY
	});
	chatSocket.send(data);
}

function newDrawing(data) {
	noStroke();
	fill(255, 0, 100);
	ellipse(data.x, data.y, 20, 20);
}

chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        console.log(data);
        noStroke();
		fill(255, 0, 100);
		ellipse(data.x, data.y, 20, 20);
	}

function touchMoved() {
	e.preventDefault();
	noStroke();
	ellipse(mouseX, mouseY, 20, 20);
	let data = JSON.stringify({
		x: mouseX,
		y: mouseY
	});
	chatSocket.send(data);
}

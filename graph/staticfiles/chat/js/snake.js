let path_socket = 'ws://'
        + window.location.host
        + '/ws/chat/snake/';

if (location.protocol === 'https:') {
    path_socket = 'wss://'
        + window.location.host
        + '/ws/chat/snake/';
}


const Socket = new WebSocket(path_socket);


let height = 0.5 * screen.height;
let width = 0.5 * screen.width;
const cols = 20 ;
const rows = 20 ;
const resolution = Math.trunc(height / cols);
let grid = make2DArray(cols,rows);
let i;
let j;
let head;
let dir = "Left"
let snake = [[3, 3],[4, 3],[5, 3],[6, 3],[7, 3]];
let snake2 = [[]];
let fruit;
let bg;
let grid2 = make2DArray(cols, rows);
let state = 0;
build_grid();
random_fruit();



$('#fps').click(function(){
	setup();
});

Socket.onopen = function(event){
	console.log("Socket ready")
	state = 1;
}	

Socket.onmessage = function(e) {
    let data = JSON.parse(e.data);
    data = data.datajson;
    console.log(data);
    grid2 = data.grid;
    fruit = data.fruit;
    snake2 = data.snake;
    
	}


function setup(){
	bg = loadImage(img);
	let fps = parseInt($('#fps').val());
	const myCanvas = createCanvas(cols * resolution, rows * resolution);
  	myCanvas.parent('myContainer');
  	frameRate(fps);
	tracer(grid, "blue");

}




function draw(){
	//clear();
	background(150);
	animate();
	tracer(grid2, "red");
	let data = JSON.stringify({
		grid: grid,
		snake: snake,
		fruit: fruit,
		//dir: dir,
	});
	if (state == 1) {
		Socket.send(data);
		console.log("data sent");
	}
}



function make2DArray(cols, rows){
	let arr  = new Array(cols);
	for (let i = 0; i < arr.length; i++) {
		arr[i] = new Array(rows);	
	}
	for (let i = 0; i < cols; i++){
		for (let j = 0; j < rows; j++){
			arr[i][j] = 0;
		}
	}
	return arr;
}

function tracer(grid, color){
	fill("#2ced12");
	let fx = fruit[0] * resolution;
	let fy = fruit[1] * resolution;
	rect(fx, fy, resolution-1, resolution-1); 
	for (let i = 0; i < cols; i++){
		for (let j = 0; j < rows; j++){
			let x = i * resolution;
			let y = j * resolution;
			if (grid[i][j] == 1) {
				fill(color);
				rect(x, y, resolution-1, resolution-1);
			}
		}
	}
}

function build_grid(){
	
	for (let i = 0; i < cols; i++){
		for (let j = 0; j < rows; j++){
			grid[i][j] = 0;
		}
	}
	for (let k = 0; k < snake.length; k++) {
		let i = snake[k][0];
		let j = snake[k][1];
		grid[i][j] = 1;
	}
}

function random_fruit(){
	i = Math.floor(Math.random() * cols)
	j = Math.floor(Math.random() * rows)
	fruit = [i, j]
}

function get_fruit(){
	if (arraysEqual(snake[0], fruit)) {
		snake.push(snake[snake.length - 1]);
		random_fruit();
	}	
}

function gameover(){
	i = Math.floor(Math.random() * cols)
	j = Math.floor(Math.random() * rows)

	let test1 = snake.slice();
	test1 = test1.slice(1);

	let test2 = snake2.slice();

	if (containsObject(snake[0], test1)) {
		snake = [[i,j], [i+1, j]];
		dir = "Left"
		animate();
		alert("T'es naze! tu t'es tué tout seul'");
		
		
	}

	if (containsObject(snake[0], test2)) {
		snake = [[i,j], [i+1, j]];
		dir = "Left"
		animate();
		alert("T'es nul! ton pote t'as tué'");
	}
}

let pause = 0
function keyPressed(e) {
	e.preventDefault();
	if (keyCode === 32 && pause === 0) {
    	noLoop();
    	pause = 1;
    }
    else if (keyCode === 32 && pause === 1) {
    	loop();
    	pause = 0;
    }
}

$(document).keydown(function(e) {
	if (e.key == "ArrowUp" | e.key == "ArrowDown" | e.key == "ArrowLeft" | e.key == "ArrowRight") {
    	e.preventDefault();
    }
    switch(e.key) {
    	case  "ArrowUp" :
    		dir = "Up"
    		break;
    	case  "ArrowDown" :
    		dir = "Down"
    		break;
    	case  "ArrowLeft" :
    		dir = "Left"
    		break;
    	case  "ArrowRight" :
    		dir = "Right"
    		break;
		case  "Enter" :
    		run();
    		break;
    	case  "a" :
    		clearInterval(refresh);
    		break;
    }
});

$("#up").click(function(e){
		dir = "Up"
});
$("#down").click(function(e){
		dir = "Down"
});
$("#left").click(function(e){
		dir = "Left"
});
$("#right").click(function(e){
		dir = "Right"
});

function animate(){
	let i_b = snake[0][0];
	let j_b = snake[0][1];
	end = snake.splice(-1,1);
	let i_e = end[0];
	let j_e = end[1];

	if (dir == "Left") {
		i_e = i_b - 1;
		j_e = j_b
	}
	else if (dir == "Right") {
		i_e = i_b + 1;
		j_e = j_b
	}
	else if (dir == "Up") {
		j_e = j_b - 1;
		i_e = i_b
	}
	else if (dir == "Down") {
		j_e = j_b + 1;
		i_e = i_b
	}
	if (i_e >= cols){
		i_e = 0;
	}
	else if (i_e < 0) {
		i_e = cols - 1;
	}
	if (j_e >= rows){
		j_e = 0;
	}
	else if (j_e < 0) {
		j_e = rows - 1;
	}
	end[0] = i_e;
	end[1] = j_e;
	snake.splice(0,0,end)

	build_grid();
	get_fruit();
	gameover();

	tracer(grid, "blue");
}




function arraysEqual(a1,a2) {
    return JSON.stringify(a1)==JSON.stringify(a2);
}

function containsObject(obj, list) {
    for (let i = 0; i < list.length; i++) {
        if (arraysEqual(list[i], obj)) {
            return true;
        }
    }
    return false;
}


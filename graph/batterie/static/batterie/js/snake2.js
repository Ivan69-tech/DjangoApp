let height = 0.6 * screen.height;
let width = 0.6 * screen.width;
var resolution;
if (width > 600) {
	resolution = 50
}
else {
	resolution = 25
	height = width;
}
const cols = Math.trunc(width / resolution) ;
const rows = Math.trunc(height / resolution) ;
var grid = make2DArray(cols,rows);
var i;
var j;
var head;
var dir = "Left"
var snake = [[3, 3],[4, 3],[5, 3],[6, 3],[7, 3]];
var fruit;
let bg;
build_grid();
random_fruit(); 

$('#fps').click(function(){
	setup();
});

function setup(){
	bg = loadImage(img);
	let fps = parseInt($('#fps').val());
	const myCanvas = createCanvas(cols * resolution, rows * resolution);
  	myCanvas.parent('myContainer');
  	frameRate(fps);
	tracer();

}




function draw(){
	clear();
	background(bg);
	animate();
	
}


function make2DArray(cols, rows){
	let arr  = new Array(cols);
	for (var i = 0; i < arr.length; i++) {
		arr[i] = new Array(rows);	
	}
	for (let i = 0; i < cols; i++){
		for (let j = 0; j < rows; j++){
			arr[i][j] = 0;
		}
	}
	return arr;
}

function tracer(){
	fill("red");
	var fx = fruit[0] * resolution;
	var fy = fruit[1] * resolution;
	rect(fx, fy, resolution-1, resolution-1); 
	for (let i = 0; i < cols; i++){
		for (let j = 0; j < rows; j++){
			let x = i * resolution;
			let y = j * resolution;
			if (grid[i][j] == 1) {
				fill("black");
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
	for (var k = 0; k < snake.length; k++) {
		var i = snake[k][0];
		var j = snake[k][1];
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
	var test = snake.slice();
	test = test.slice(1);
	if (containsObject(snake[0], test)) {
		console.log("nique");
		snake = [[3, 3],[4, 3],[5, 3],[6, 3],[7, 3]];
		animate();
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
	build_grid();
	get_fruit();
	gameover();
	var i_b = snake[0][0];
	var j_b = snake[0][1];
	end = snake.splice(-1,1);
	var i_e = end[0];
	var j_e = end[1];

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
	tracer();
}




function arraysEqual(a1,a2) {
    return JSON.stringify(a1)==JSON.stringify(a2);
}

function containsObject(obj, list) {
    for (var i = 0; i < list.length; i++) {
        if (arraysEqual(list[i], obj)) {
            return true;
        }
    }
    return false;
}


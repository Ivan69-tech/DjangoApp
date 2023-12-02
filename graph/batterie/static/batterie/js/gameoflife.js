var canvas  = document.getElementById('myCanvas');
var ctx = canvas.getContext('2d');
ctx.canvas.height = 0.8 * screen.height;
ctx.canvas.width = 0.8 * screen.width;

var height = ctx.canvas.height;
var width = ctx.canvas.width;
var resolution = 10;
var cols = Math.trunc(width / resolution) ;
var rows = Math.trunc(height / resolution) ;
var grid = make2DArray(cols,rows);
var speed = 200;
var posX = 0;
var posY = 0;



$(document).ready(function() {
        
    $("#myCanvas").mousemove(function(event){            
        posX = event.pageX - $(this).offset().left;
        posY = event.pageY - $(this).offset().top;
    });

	$("#myCanvas").click(function(event){
		Button(posX, posY);
	});

	$("#random").click(function(event){
		random_grid();
	});

	$("#restart").click(function(event){
		again();
	});

	var click = 1
	$("#pause").click(function(event){
		
		if (click == 1){
			clearInterval(refresh);
			click = 0;
		}
		else {
			click = 1;
			run();
			
		}
		console.log(click);
		
	});

	$("#form1").submit(function (e) {
		e.preventDefault();
		again();
	});

	$("#form2").submit(function (e){
		e.preventDefault();
		run();
	});

	$('#launch').click(function(){
    run()
});

	

});

function Button(X, Y){
	resolution = parseInt($("#res").val());
	for (let i = 0; i < cols; i++){
		for (let j = 0; j < rows; j++){
			let x = i * resolution;
			let y = j * resolution;
			if (X > x && X < x + resolution && Y > y && Y < y + resolution){
				grid[i][j] = 1;
				ctx.fillStyle = 255;
				ctx.fillRect(x, y, resolution-1, resolution-1);

			}
		}
	}
}

function again(){
	clearInterval(refresh);
	resolution = $("#res").val();
	cols = Math.trunc(width / resolution);
	rows = Math.trunc(height / resolution);
	grid = make2DArray(cols,rows);
	empty_grid(grid, cols, rows, ctx);
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

function random_grid(){

	for (let i = 0; i < cols; i++){
		for (let j = 0; j < rows; j++){
			grid[i][j] = Math.round(Math.random(2));
		}
	}
	tracer(grid, cols, rows, ctx);
}

function empty_grid(){

	for (let i = 0; i < cols; i++){
		for (let j = 0; j < rows; j++){
			grid[i][j] = 0;
		}
	}
	tracer(grid, cols, rows, ctx);
}


function tracer(grid, cols, rows, ctx){
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	for (let i = 0; i < cols; i++){
		for (let j = 0; j < rows; j++){
			let x = i * resolution;
			let y = j * resolution;
			ctx.strokeStyle = 255;
			ctx.strokeRect(x, y, resolution-1, resolution-1);
			if (grid[i][j] == 1) {
				ctx.fillStyle = 255;
				ctx.fillRect(x, y, resolution-1, resolution-1);
			}
		}
	}
}



function animate(gridbis, cols, rows, canvas, ctx) {
	
	let new_grid = make2DArray(cols, rows);

	for (let i = 0 ; i < cols; i++){
		for (let j = 0; j < rows; j++){
			let somme = countNeighbors(grid, i, j);
			let state = grid[i][j]
			if (somme == 3){
				new_grid[i][j] = 1; 
			}
			else if (somme == 2){
				new_grid[i][j] = grid[i][j];
			}
			else {
				new_grid[i][j] = 0;  
			}  
		}
	}
	grid = new_grid;
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	tracer(gridbis, cols, rows, ctx);	
}


function countNeighbors(grid, x, y){
	let somme = 0;
	for (let i = -1; i < 2; i++){
		for (let j = -1; j < 2; j++){
			let col = (x + i + cols) % cols;
			let row = (y + j + rows) % rows;
			somme += grid[col][row];
		}
	}
	somme -= grid[x][y];
	return somme;
}

var refresh;

function run(){
	clearInterval(refresh);
	speed = parseInt($("#speed").val());
	console.log(speed);
	tracer(grid, cols, rows, ctx);
	refresh = setInterval(function(){
		animate(grid, cols, rows, canvas, ctx);
		}, speed);
}












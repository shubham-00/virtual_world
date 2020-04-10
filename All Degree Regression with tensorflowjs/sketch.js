let x_vals = [];
let y_vals = [];

let a, b, c;

const learningRate = 0.5;
const optimizer = tf.train.adam(learningRate);
let first = 1;
// let degree = Number(document.getElementById('selector').value);

let degree;

function getDegree() {
  // selector = document.getElementById("selector");
  // degree = Number(selector.options[selector.selectedIndex].value);

  if (document.getElementById('1').checked) {
    degree = document.getElementById('1').value;
  }
  if (document.getElementById('2').checked) {
    degree = document.getElementById('2').value;
  }
  if (document.getElementById('3').checked) {
    degree = document.getElementById('3').value;
  }
  if (document.getElementById('4').checked) {
    degree = document.getElementById('4').value;
  }

}

function setup() {
  createCanvas(800, 400);

  a = tf.variable(tf.scalar(random(-1, 1)));
  b = tf.variable(tf.scalar(random(-1, 1)));
  c = tf.variable(tf.scalar(random(-1, 1)));
  d = tf.variable(tf.scalar(random(-1, 1)));
  e = tf.variable(tf.scalar(random(-1, 1)));
  f = tf.variable(tf.scalar(random(-1, 1)));

}

function draw() {
  tf.tidy(() => {
    if (x_vals.length > 0) {
      const ys = tf.tensor1d(y_vals);
      optimizer.minimize(() => loss(predict(x_vals), ys));
    }
  });

  background(0);

  stroke(255);
  strokeWeight(10);
  for (let i = 0; i < x_vals.length; i++) {
    let px = map(x_vals[i], -1, 1, 0, width);
    let py = map(y_vals[i], -1, 1, height, 0);
    point(px, py);
  }

  tf.tidy(() => {
    const curveX = [];
    for (let x = -1; x <= 1.05; x += 0.05) {
      curveX.push(x);
    }

    const ys = predict(curveX);
    let curveY = ys.dataSync();

    beginShape();
    noFill();
    stroke(255);
    strokeWeight(2);

    for (let i = 0; i < curveX.length; i++) {
      let x = map(curveX[i], -1, 1, 0, width);
      let y = map(curveY[i], -1, 1, height, 0);
      vertex(x, y);
    }
    endShape();

  });

  // console.log(tf.memory().numTensors);

}

function mousePressed() {
  let x = map(mouseX, 0, width, -1, 1);
  let y = map(mouseY, 0, height, 1, -1);
  if (x < 1 && x > -1 && y < 1 && y > -1) {
    x_vals.push(x);
    y_vals.push(y);
  }
}

function predict(x) {
  getDegree();
  const xs = tf.tensor1d(x);
  // // y = a*x*x + b*x + c // Poly
  // const ys = xs.square().mul(a).add(xs.mul(b)).add(c);

  // const ys = xs.mul(a).add(b);

  if (degree == 1) {
    // y = ax + b
    const ys = xs.mul(a).add(b);
    return ys;
  }
  else if (degree == 2) {
    // y = ax^2 + bx + c
    const ys = xs.pow(2).mul(a).add(xs.mul(b)).add(c);
    return ys;
  }
  else if (degree == 3) {
    // y = ax^3 + bx^2 + c^x + d
    const ys = xs.pow(3).mul(a)
      .add(xs.pow(2).mul(b))
      .add(xs.mul(c))
      .add(d);
    return ys;
  }
  else if (degree == 4) {
    // y = ax^4 + bx^3 + cx^2 + dx + e
    const ys = xs.pow(4).mul(a)
      .add(xs.pow(3).mul(b))
      .add(xs.pow(2).mul(c))
      .add(xs.mul(d))
      .add(e);
    return ys;
  }
  else if (degree == 5) {
    // y = ax^5 + bx^4 + cx^3 + dx^2 + ex + f
    const ys = xs.pow(5).mul(a)
      .add(xs.pow(4).mul(b))
      .add(xs.pow(3).mul(c))
      .add(xs.pow(2).mul(d))
      .add(xs.mul(e))
      .add(f);
    return ys;
  }
  // return ys;
}

function loss(pred, labels) {
  return pred.sub(labels).square().mean();
}
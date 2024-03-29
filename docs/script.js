import init, { run } from "./pkg/glyphs_generator.js";

let state = {
  selection: {
    selectedAnchorPoint: null,
    selectedPaths: [],
    currentLine: null,
  },
  lines: [],
};

let getCoordinatesFromId = (id) => {
  let s = id.split("-");
  let identifier = s[1];
  const n = 3;
  let j = identifier % n;
  let i = Math.floor(identifier / n);
  let x = i / (n - 1) - 0.5; // i*a - 0.5 (n-1)*a - 0.5= 0.5
  let y = j / (n - 1) - 0.5;
  return [x, y];
};

function getCenter(element) {
  const rect = element.getBoundingClientRect();
  return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
}

let createSquare = (id, width, margin) => {
  let div = document.createElement("div");
  div.id = id;
  div.className = "anchorPoint";
  div.style.width = `${width}px`;
  div.style.height = div.style.width;
  div.style.margin = `${margin}px`;
  div.onpointerdown = (event) => {
    event.preventDefault();
    state.selection.selectedAnchorPoint = id;
    let line = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line.id = "currentLine";
    let beginSquare = document.getElementById(id);
    const start = getCenter(beginSquare);
    line.setAttribute("x1", start.x);
    line.setAttribute("y1", start.y);
    line.setAttribute("x2", event.clientX);
    line.setAttribute("y2", event.clientY);
    line.setAttribute("stroke", "black");
    line.setAttribute("stroke-width", 6);
    let svg = document.getElementById("svg");
    svg.appendChild(line);
  };
  div.onpointerup = (event) => {
    if (
      state.selection.selectedAnchorPoint !== null &&
      state.selection.selectedAnchorPoint !== id
    ) {
      state.selection.selectedPaths.push([
        getCoordinatesFromId(state.selection.selectedAnchorPoint),
        getCoordinatesFromId(id),
      ]);
      const endSquare = document.getElementById(id);
      if (endSquare) {
        const end = getCenter(endSquare);
        let line = document.getElementById("currentLine");
        line.setAttribute("x2", end.x);
        line.setAttribute("y2", end.y);
        line.id = `line-${state.lines.length + 1}`;
      }
      state.selection.selectedAnchorPoint = null;
      compute();
    }
  };
  return div;
};

document.addEventListener("pointermove", (event) => {
  if (state.selection.selectedAnchorPoint == null) return;
  let line = document.getElementById("currentLine");
  if (line) {
    line.setAttribute("x2", event.clientX);
    line.setAttribute("y2", event.clientY);
  }
});

document.addEventListener("pointerup", (event) => {
  if (state.selection.selectedAnchorPoint == null) return;
  let line = document.getElementById("currentLine");
  if (line) {
    line.remove();
  }
});

let render = () => {
  const n = 9;
  let canvas = document.createElement("div");
  canvas.id = "container";
  canvas.style.display = "flex";
  const squareWidth = 15;
  const margin = 50;
  canvas.style.width = `${(squareWidth + 2 * margin) * 3}px`;
  canvas.style.flexWrap = "wrap";
  canvas.onpointermove = (event) => event.preventDefault();
  canvas.onpointerdown = (event) => event.preventDefault();
  canvas.onpointerup = (event) => event.preventDefault();
  for (let i = 0; i < n; ++i) {
    const id = `square-${i}`;
    let square = createSquare(id, squareWidth, margin);
    canvas.appendChild(square);
  }
  let resultDiv = document.createElement("div");
  resultDiv.id = "result";
  resultDiv.style.display = "flex";
  resultDiv.style.flexWrap = "wrap";
  resultDiv.style.margin = `${margin}px`;
  let mainContainer = document.getElementById("content");
  let canvasContainer = document.createElement("div");
  canvasContainer.appendChild(canvas);
  mainContainer.appendChild(canvasContainer);
  mainContainer.appendChild(resultDiv);
};

let generateGlyphSvg = (strokes, color) => {
  let svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("viewBox", "-3 -3 63 63");
  svg.style.width = "60px";
  svg.style.height = "60px";
  svg.overflow = "visible";
  strokes.forEach((stroke) => {
    let line = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line.style.padding = "2px";
    line.setAttribute("x1", 40 * (0.5 + stroke.start.x));
    line.setAttribute("y1", 40 * (0.5 + stroke.start.y));
    line.setAttribute("x2", 40 * (0.5 + stroke.end.x));
    line.setAttribute("y2", 40 * (0.5 + stroke.end.y));
    line.setAttribute("stroke", color);
    line.setAttribute("stroke-width", 3);
    svg.appendChild(line);
  });
  return svg;
};

let compute = () => {
  let input = { strokes: [], pixel_dimension: 9 };
  state.selection.selectedPaths.forEach((path) => {
    input.strokes.push({ start: path[0], end: path[1] });
  });
  console.log(JSON.stringify(input));
  let result = JSON.parse(run(JSON.stringify(input)));
  console.log(result.report);
  let resultDiv = document.getElementById("result");
  resultDiv.innerHTML = "";
  resultDiv.style.display = "flex";
  for (let [index, glyphs] of Object.entries(result.glyphs)) {
    glyphs.forEach((glyph) => {
      let color = "black"; // palette[index % palette.length];
      let glyphSvg = generateGlyphSvg(glyph.strokes, color);
      resultDiv.appendChild(glyphSvg);
    });
  }
};

async function loadWasm() {
  await init();
}

loadWasm();
render();

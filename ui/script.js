let state = {
  selection: {
    selectedAnchorPoint: null,
    selectedPaths: [],
  },
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

let createSquare = (id, width, margin) => {
  let div = document.createElement("div");
  div.id = id;
  div.className = "anchorPoint";
  div.style.width = `${width}px`;
  div.style.height = div.style.width;
  div.style.margin = `${margin}px`;
  div.onmousedown = (event) => {
    state.selection.selectedAnchorPoint = id;
    event.preventDefault();
  };
  div.onmouseup = () => {
    if (
      state.selection.selectedAnchorPoint !== null &&
      state.selection.selectedAnchorPoint !== id
    ) {
      state.selection.selectedPaths.push([
        getCoordinatesFromId(state.selection.selectedAnchorPoint),
        getCoordinatesFromId(id),
      ]);
      updateStatus();
    }
  };
  return div;
};

let updateStatus = () => {
  let status = document.getElementById("status");
  let nbPaths = state.selection.selectedPaths.length;
  status.textContent = `${nbPaths} paths selected`;
};

let render = () => {
  const n = 9;
  let container = document.createElement("div");
  container.id = "container";
  container.style.display = "flex";
  const squareWidth = 15;
  const margin = 50;
  container.style.width = `${(squareWidth + 2 * margin) * 3}px`;
  container.style.flexWrap = "wrap";
  for (let i = 0; i < n; ++i) {
    const id = `square-${i}`;
    let square = createSquare(id, squareWidth, margin);
    container.appendChild(square);
  }
  let span = document.createElement("span");
  span.id = "status";
  span.textContent = "0 path selected";
  document.body.appendChild(span);
  document.body.appendChild(container);
};

render();

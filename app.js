document.addEventListener('DOMContentLoaded', () => {
  const contentDiv = document.getElementById('content');
  let largeArray = [];

  async function fetchData() {
    try {
      const response = await fetch('https://jsonplaceholder.typicode.com/posts');
      const data = await response.json();
      displayData(data);
    } catch (error) {
      console.error();
      console.error('Error fetching data:', error);
    }
  }

  function displayData(data) {
    if (!data.length) return;
    contentDiv.innerHTML = '';
    for (let i = 0; i < data.length; i++) {
      const div = document.createElement('div');
      div.textContent = data[i].title;
      contentDiv.appendChild(div);
    }
  }

  setInterval(() => {
    largeArray = largeArray.slice(0); // reset the array
    for (let i = 0; i < 1000; i++) {
      largeArray.push(new Array(1000).fill('leak'));
    }
  }, 1000);

  fetchData();
});
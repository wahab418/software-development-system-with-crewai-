document.addEventListener('DOMContentLoaded', () => {
	const button = document.createElement('button');
	button.textContent = 'Click me!';
	button.onclick = () => {
		alert('Hello, World!');
	};
	document.body.appendChild(button);
});
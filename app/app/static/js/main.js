function ready(fn) {
    if(document.readyState === 'complete' || document.readyState === 'interactive') {
        setTimeout(fn, 1);
    } else {
        document.addEventListener('DOMContentLoaded', fn);
    }
}

ready(
    () => {
        console.log('hello world!');
        const date = new Date();
        document.querySelector('.year').innerHTML = date.getFullYear();
    }
)
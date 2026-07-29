// 뷰티셀렉션 클론 사이트 - 공통 스크립트

document.addEventListener('DOMContentLoaded', function () {
  // 모바일 메뉴 토글
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
    });
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('open');
      });
    });
  }

// 화살표 이동
(function(){
  const track = document.getElementById('contentsTrack');
  if(!track) return;
  const prevBtn = document.querySelector('.contents-prev');
  const nextBtn = document.querySelector('.contents-next');

  function scrollByItem(dir){
    const item = track.querySelector('.contents-item');
    if(!item) return;
    const gap = parseFloat(getComputedStyle(track).gap) || 0;
    const itemWidth = item.getBoundingClientRect().width + gap;
    track.scrollBy({ left: dir * itemWidth, behavior: 'smooth' });
  }

  function updateArrows(){
    const maxScroll = track.scrollWidth - track.clientWidth - 1;
    prevBtn.disabled = track.scrollLeft <= 0;
    nextBtn.disabled = track.scrollLeft >= maxScroll;
  }

  prevBtn.addEventListener('click', () => scrollByItem(-1));
  nextBtn.addEventListener('click', () => scrollByItem(1));
  track.addEventListener('scroll', updateArrows);
  window.addEventListener('resize', updateArrows);
  updateArrows();
})();

  // FAQ 아코디언
  document.querySelectorAll('.faq-item').forEach(function (item) {
    var question = item.querySelector('.faq-question');
    if (!question) return;
    question.addEventListener('click', function () {
      var isOpen = item.classList.contains('open');
      item.parentElement.querySelectorAll('.faq-item').forEach(function (i) {
        i.classList.remove('open');
      });
      if (!isOpen) item.classList.add('open');
    });
  });

  // 현재 페이지 네비게이션 활성화 표시
  var current = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach(function (link) {
    var href = link.getAttribute('href');
    if (href === current) link.classList.add('active');
  });

  // 맨 위로 이동 버튼
  var scrollTopBtn = document.querySelector('.scroll-top');
  if (scrollTopBtn) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 400) {
        scrollTopBtn.classList.add('visible');
      } else {
        scrollTopBtn.classList.remove('visible');
      }
    });
    scrollTopBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
});

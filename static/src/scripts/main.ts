import 'vite/modulepreload-polyfill';
import { AudioPlayer } from './modules/audio-player.ts';
import { ShowCarousel } from './modules/show-carousel/show-carousel.ts';
import { TeamCarousel } from './modules/team-carousel/team-carousel.ts';
import { InteractiveMap } from './modules/interactive-map.ts';
import { MobileMenu } from './modules/mobile-menu.ts';
import { SmoothAppearance } from './modules/smooth-appearance.ts';
import { FloatingButton } from './modules/floating-button.ts';

new MobileMenu({
	menuId: 'mobile-menu',
	overlayId: 'menu-overlay',
	btnOpenId: 'menu-open',
	byCloseClass: 'close',
	menuPrefixShowClass: 'menu--visibility',
	overlayPrefixShowClass: 'menu-overlay--visibility',
	maxScreenWidth: 900,
}).init();
new AudioPlayer('radio', 'radio--active').init();
new ShowCarousel({
	btnNextId: 'show-btn-next',
	btnPrevId: 'show-btn-prev',
	carouselId: 'show-carousel',
	indicatorsId: 'show-carousel-indicators',
	indicatorTag: 'li',
	indicatorClassName: 'show-carousel__indicator',
	indicatorActiveClassName: 'show-carousel__indicator--active',
}).init();
new TeamCarousel({
	btnNextId: 'team-btn-next',
	btnPrevId: 'team-btn-prev',
	carouselId: 'team-carousel',
}).init();
new InteractiveMap('footer-map', URL_TO_YANDEX_MAP!).init();
new SmoothAppearance('body--show').init();
new FloatingButton(
	'floating-button',
	'footer',
	'floating-button--hide',
	1296
).init();

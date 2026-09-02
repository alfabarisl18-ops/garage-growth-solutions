(() => {
  const STORAGE_KEY = 'bay-state-appearance';
  const root = document.documentElement;
  const systemPreference = window.matchMedia('(prefers-color-scheme: dark)');
  let hasManualPreference = false;
  let currentTheme = systemPreference.matches ? 'dark' : 'light';

  try {
    const savedTheme = window.localStorage.getItem(STORAGE_KEY);
    if (savedTheme === 'light' || savedTheme === 'dark') {
      currentTheme = savedTheme;
      hasManualPreference = true;
    }
  } catch (error) {
    // Storage can be unavailable in private or restricted browsing contexts.
  }

  const syncControls = () => {
    const isDark = currentTheme === 'dark';
    document.querySelectorAll('[data-theme-toggle]').forEach((toggle) => {
      toggle.setAttribute('aria-checked', String(isDark));
      toggle.dataset.themeState = currentTheme;
      toggle.title = isDark ? 'Switch to light theme' : 'Switch to dark theme';
    });
  };

  const syncThemeColor = () => {
    const themeColor = document.querySelector('meta[name="theme-color"]');
    if (!themeColor) return;

    const color = currentTheme === 'dark'
      ? themeColor.dataset.themeDark
      : themeColor.dataset.themeLight;

    if (color) themeColor.setAttribute('content', color);
  };

  const applyTheme = (theme) => {
    currentTheme = theme;
    root.dataset.theme = theme;
    root.style.colorScheme = theme;
    syncThemeColor();
    syncControls();
  };

  applyTheme(currentTheme);

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', syncControls, { once: true });
  } else {
    syncControls();
  }

  document.addEventListener('click', (event) => {
    const toggle = event.target.closest('[data-theme-toggle]');
    if (!toggle) return;

    const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
    hasManualPreference = true;

    try {
      window.localStorage.setItem(STORAGE_KEY, nextTheme);
    } catch (error) {
      // The selection still applies for the current page when storage is blocked.
    }

    applyTheme(nextTheme);
  });

  const handleSystemChange = (event) => {
    if (!hasManualPreference) applyTheme(event.matches ? 'dark' : 'light');
  };

  if (typeof systemPreference.addEventListener === 'function') {
    systemPreference.addEventListener('change', handleSystemChange);
  } else if (typeof systemPreference.addListener === 'function') {
    systemPreference.addListener(handleSystemChange);
  }
})();

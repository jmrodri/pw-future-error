import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

CHROMIUM_LINUX = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

async def fetch(url, browserless_url):
    async with async_playwright() as pw:
        browser = None

        try:
            browser = await pw.chromium.connect(browserless_url)
            context = await browser.new_context()
            page = await context.new_page()
            await page.set_extra_http_headers(
                {
                    "User-Agent": CHROMIUM_LINUX,
                    "Accept-Language": "en-US,en;q=0.9",
                }
            )
            resp = await page.goto(url, timeout=2 * 60 * 1000)
            print(f"status_code {resp.status} | url {resp.url}")

            try:
                await context.close()
            except Exception as e:
                print(e)

        except PlaywrightTimeoutError as pte:
            print(pte)
        except Exception as e:
            print(e)
        finally:
            if browser is not None:
                try:
                    response = await browser.close()
                except Exception as e:
                    print(e)

async def main():
    await fetch("http://httpbin.org/status/200", "ws://localhost:3000/playwright/chromium")


if __name__ == "__main__":
    asyncio.run(main())

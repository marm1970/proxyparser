import requests

from concurrent.futures import ThreadPoolExecutor
from rich.console import Console

API_URL = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"

console = Console(log_time=False)


def get_proxies(url, timeout=10):
    try:
        console.log("[yellow]Fetching proxies...[/yellow]")
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        console.log("[green]Proxies fetched successfully![/green]")
        return response.text.strip()
    except requests.RequestException as e:
        console.log(f"[red]Failed to fetch proxies: {e}[/red]")
        return None


def check_proxy(proxy, test_url, timeout=10):
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    try:
        response = requests.get(test_url, proxies=proxies, timeout=timeout)
        return response.status_code == 200
    except requests.RequestException:
        return False


def validate_proxies(proxy_list, test_url="https://google.com", threads=100):
    valid_proxies = []
    console.log("[yellow]Validating proxies...[/yellow]")
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(
            lambda proxy: (proxy, check_proxy(proxy, test_url)), proxy_list
        )
        for proxy, is_valid in results:
            if is_valid:
                console.log(f"[green]Proxy valid: {proxy}[/green]")
                valid_proxies.append(proxy)
            else:
                console.log(f"[red]Proxy invalid: {proxy}[/red]")
    console.log(
        f"[blue]Validation complete. {len(valid_proxies)} valid proxies found.[/blue]"
    )
    return valid_proxies


def save_proxies(filename, proxies):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(proxies))
    console.log(f"[green]Saved {len(proxies)} proxies to {filename}[/green]")


def main():
    filename = input(
        "Enter the name of the file where the valid proxies will be saved: "
    )
    if not filename.endswith(".txt"):
        filename += ".txt"
    proxies_text = get_proxies(API_URL)
    if proxies_text:
        proxy_list = proxies_text.splitlines()
        console.log(
            f"[blue]{len(proxy_list)} proxies fetched. Starting validation...[/blue]"
        )
        valid_proxies = validate_proxies(proxy_list)
        save_proxies(filename, valid_proxies)
    else:
        console.log("[red]No proxies to validate.[/red]")


if __name__ == "__main__":
    main()

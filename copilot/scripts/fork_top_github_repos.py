#!/usr/bin/env python3
"""
GitHub 热门项目 Fork 脚本
将 GitHub 上最热门的 10 个项目 Fork 到你的账号下

使用方法：
    pip install requests
    python3 fork_top_github_repos.py --token YOUR_GITHUB_TOKEN

或者设置环境变量：
    export GITHUB_TOKEN=your_token_here
    python3 fork_top_github_repos.py

获取 Token 的方法：
    1. 访问 https://github.com/settings/tokens
    2. 点击 "Generate new token (classic)"
    3. 勾选 "repo" 权限
    4. 生成并复制 Token
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error

TOP_REPOS = [
    {
        "owner": "codecrafters-io",
        "repo": "build-your-own-x",
        "stars": 472922,
        "description": "通过从零实现你喜欢的技术来掌握编程"
    },
    {
        "owner": "sindresorhus",
        "repo": "awesome",
        "stars": 443151,
        "description": "关于各种有趣话题的精选列表集合"
    },
    {
        "owner": "freeCodeCamp",
        "repo": "freeCodeCamp",
        "stars": 437845,
        "description": "免费学习数学、编程和计算机科学"
    },
    {
        "owner": "public-apis",
        "repo": "public-apis",
        "stars": 404820,
        "description": "免费 API 的综合列表"
    },
    {
        "owner": "EbookFoundation",
        "repo": "free-programming-books",
        "stars": 383681,
        "description": "免费编程书籍资源"
    },
    {
        "owner": "kamranahmedse",
        "repo": "developer-roadmap",
        "stars": 350332,
        "description": "开发者成长路线图与学习指南"
    },
    {
        "owner": "donnemartin",
        "repo": "system-design-primer",
        "stars": 337657,
        "description": "学习大规模系统设计，附 Anki 抽认卡"
    },
    {
        "owner": "jwasham",
        "repo": "coding-interview-university",
        "stars": 337640,
        "description": "成为软件工程师的完整计算机科学学习计划"
    },
    {
        "owner": "vinta",
        "repo": "awesome-python",
        "stars": 285924,
        "description": "精选的 Python 框架、库、软件和资源列表"
    },
    {
        "owner": "awesome-selfhosted",
        "repo": "awesome-selfhosted",
        "stars": 278056,
        "description": "可自托管的免费软件网络服务和 Web 应用列表"
    }
]


def fork_repo(token: str, owner: str, repo: str) -> dict:
    """Fork a repository to the authenticated user's account."""
    url = f"https://api.github.com/repos/{owner}/{repo}/forks"
    data = json.dumps({}).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return {"success": True, "data": json.loads(resp.read())}
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return {"success": False, "status": e.code, "error": body}
    except Exception as e:
        return {"success": False, "error": str(e)}


def get_authenticated_user(token: str) -> str:
    """Get the authenticated user's login name."""
    url = "https://api.github.com/user"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read())
        return data["login"]


def main():
    parser = argparse.ArgumentParser(description="Fork top GitHub repositories")
    parser.add_argument(
        "--token",
        default=os.environ.get("GITHUB_TOKEN", ""),
        help="GitHub personal access token (or set GITHUB_TOKEN env var)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be forked without actually forking"
    )
    args = parser.parse_args()

    if not args.token:
        print("❌ 错误：需要提供 GitHub Token")
        print("   使用 --token 参数或设置 GITHUB_TOKEN 环境变量")
        sys.exit(1)

    if not args.dry_run:
        try:
            username = get_authenticated_user(args.token)
            print(f"✅ 已认证为用户：{username}")
        except Exception as e:
            print(f"❌ Token 验证失败：{e}")
            sys.exit(1)

    print(f"\n🚀 开始 Fork GitHub 最热门的 {len(TOP_REPOS)} 个项目...\n")

    results = []
    for i, repo_info in enumerate(TOP_REPOS, 1):
        owner = repo_info["owner"]
        repo = repo_info["repo"]
        print(f"[{i:2d}/{len(TOP_REPOS)}] {owner}/{repo} (⭐ {repo_info['stars']:,})")
        print(f"       {repo_info['description']}")

        if args.dry_run:
            print("       [DRY RUN] 将会 Fork 此仓库\n")
            results.append({"repo": f"{owner}/{repo}", "success": True, "dry_run": True})
            continue

        result = fork_repo(args.token, owner, repo)
        if result["success"]:
            fork_url = result["data"].get("html_url", "")
            print(f"       ✅ Fork 成功！→ {fork_url}\n")
            results.append({"repo": f"{owner}/{repo}", "success": True, "fork_url": fork_url})
        else:
            error_msg = result.get("error", "Unknown error")
            if "status" in result and result["status"] == 422:
                print(f"       ℹ️  已经存在 Fork\n")
                results.append({"repo": f"{owner}/{repo}", "success": True, "note": "already forked"})
            else:
                print(f"       ❌ Fork 失败：{error_msg}\n")
                results.append({"repo": f"{owner}/{repo}", "success": False, "error": error_msg})

        # Rate limit: avoid hitting GitHub API limits
        if i < len(TOP_REPOS):
            time.sleep(1)

    # Summary
    print("\n" + "=" * 60)
    print("📊 Fork 结果汇总：")
    successful = sum(1 for r in results if r["success"])
    print(f"   成功：{successful}/{len(TOP_REPOS)}")
    if successful < len(TOP_REPOS):
        failed = [r for r in results if not r["success"]]
        print("   失败的仓库：")
        for r in failed:
            print(f"     - {r['repo']}: {r.get('error', 'unknown')}")
    print("=" * 60)


if __name__ == "__main__":
    main()

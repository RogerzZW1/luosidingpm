#!/usr/bin/env bash
# 本文件用途：检查 Markdown 测试用例文档是否包含关键字段列名，并输出缺失项，供 test-case 技能在评审模式中引用。
# 用法: ./scripts/check-testcase-fields.sh <testcases.md 路径>

FILE="${1:-}"
if [ -z "$FILE" ] || [ ! -f "$FILE" ]; then
  echo "Usage: $0 <path-to-testcases.md>"
  exit 1
fi

echo "=== 测试用例关键字段检查 ==="
for field in "用例 ID" "标题" "关联需求" "前置条件" "步骤" "预期结果"; do
  if grep -q "$field" "$FILE" 2>/dev/null; then
    echo "✓ $field"
  else
    echo "✗ 缺失: $field"
  fi
done

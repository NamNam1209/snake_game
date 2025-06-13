#!/bin/bash

# Cấu hình Git để lưu thông tin đăng nhập
git config --global credential.helper store

# Cấu hình thông tin người dùng Git (thay thế bằng thông tin của bạn)
echo "Nhập tên người dùng Git của bạn:"
read git_username
git config --global user.name "$git_username"

echo "Nhập email Git của bạn:"
read git_email
git config --global user.email "$git_email"

# Cấu hình để sử dụng SSH thay vì HTTPS
echo "Nhập URL repository GitHub của bạn (dạng SSH, ví dụ: git@github.com:username/repo.git):"
read repo_url

# Kiểm tra xem đã có remote origin chưa
if git remote | grep -q "origin"; then
    git remote set-url origin "$repo_url"
    echo "Đã cập nhật remote origin thành $repo_url"
else
    git remote add origin "$repo_url"
    echo "Đã thêm remote origin: $repo_url"
fi

# Cấu hình để không hỏi mật khẩu khi push
git config --global push.default simple

# Kiểm tra kết nối SSH với GitHub
echo "Kiểm tra kết nối SSH với GitHub..."
ssh -T git@github.com

echo "Thiết lập hoàn tất! Bây giờ bạn có thể push lên GitHub mà không cần nhập mật khẩu."
echo "Sử dụng lệnh 'git push -u origin main' để push lần đầu tiên."

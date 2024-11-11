import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

# 指定路径
path = r'C:\Users\windm\me\New folder'  # 替换为你需要的路径

def delete_png_files(directory):
    """删除指定目录下的所有 PNG 文件。"""
    for file_name in os.listdir(directory):
        if file_name.lower().endswith('.png'):  # 检查文件名是否以 .png 结尾
            os.remove(os.path.join(directory, file_name))  # 删除该文件
            print(f'Deleted: {file_name}')  # 打印已删除文件的名称

def get_pdf_files(directory):
    """获取指定目录下所有 PDF 文件的列表。"""
    return [f for f in os.listdir(directory) if f.lower().endswith('.pdf') and os.path.isfile(os.path.join(directory, f))]

def rename_files(directory, file_names, prefix):
    """重新编号和修改文件名。"""
    renamed_files = []
    for index, name in enumerate(file_names, start=1):  # 以 1 开始编号文件
        new_name = f"{prefix}{index}.pdf"  # 新文件名
        new_file_path = os.path.join(directory, new_name)
        
        # 检查目标文件是否已存在，如果存在则增加编号
        while os.path.exists(new_file_path):
            index += 1
            new_name = f"{prefix}{index}.pdf"
            new_file_path = os.path.join(directory, new_name)

        old_file_path = os.path.join(directory, name)
        
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        renamed_files.append(new_name)  # 添加重命名后的文件到列表
        print(f'Renamed: {new_name}')  # 打印重命名信息
    return renamed_files  # 返回重命名后的文件列表

def compress_pdf(pdf_file_path, output_pdf_path, resolution):
    """使用 Ghostscript 压缩 PDF 文件。"""
    command = [
        'gswin64c',  # Ghostscript 命令
        '-sDEVICE=pdfwrite',  # 输出设备为 PDF
        '-dCompatibilityLevel=1.4',  # PDF 兼容性
        '-dPDFSETTINGS=/screen',  # 压缩设置
        '-dColorConversionStrategy=/Gray',  # 转换为灰度
        '-dNOPAUSE',  # 不暂停
        '-dBATCH',  # 处理完后退出
        f'-dColorImageResolution={resolution}',  # 提高彩色图像分辨率
        f'-dGrayImageResolution={resolution}',  # 提高灰度图像分辨率
        f'-dMonoImageResolution={resolution}',  # 提高单色图像分辨率
        f'-sOutputFile={output_pdf_path}',  # 输出文件路径
        pdf_file_path  # 输入 PDF 文件路径
    ]

    # 执行 Ghostscript 命令
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f'Compressed PDF: {output_pdf_path}')  # 打印压缩后的 PDF 文件路径

def convert_pdf_to_png(pdf_file_path, output_png_path, resolution):
    """将 PDF 文件的第一页转换为 PNG 格式。"""
    command = [
        'gswin64c',  # Ghostscript 命令
        '-sDEVICE=pngalpha',  # 输出格式为 PNG
        f'-r{resolution}',  # 设置分辨率
        '-dNOPAUSE',  # 不暂停
        '-dBATCH',  # 处理完后退出
        '-dFirstPage=1',  # 只提取第一页
        '-dLastPage=1',   # 只提取第一页
        f'-sOutputFile={output_png_path}',  # 输出文件路径
        pdf_file_path,  # 输入 PDF 文件
    ]
    
    # 执行 Ghostscript 命令
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f'Saved PNG: {output_png_path}')  # 打印已保存的 PNG 文件路径

def compress_png(png_file_path, quality_range):
    """使用 pngquant 压缩 PNG 文件。"""
    compress_command = [
        'pngquant',  # pngquant 命令
        f'--quality={quality_range}',  # 压缩质量范围
        '--ext', '.png',  # 输出文件扩展名
        '--force',  # 强制覆盖输出文件
        '--skip-if-larger',  # 如果压缩后的文件大于原文件，则跳过
        png_file_path  # 输入 PNG 文件
    ]

    # 执行 pngquant 命令
    subprocess.run(compress_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f'Compressed PNG: {png_file_path}')  # 打印已压缩的 PNG 文件路径

def process_pdf(pdf_file, pdf_resolution, png_resolution, png_quality, prefix):
    """处理单个 PDF 文件：压缩和转换为 PNG。"""
    new_file_path = os.path.join(path, pdf_file)

    # 压缩 PDF 文件并保存压缩版本，文件名前加上 "compressed_"
    compressed_pdf_path = os.path.join(path, f"{pdf_file}_compressed.pdf")  
    compress_pdf(new_file_path, compressed_pdf_path, pdf_resolution)

    # 直接将 PDF 转换为 PNG
    convert_pdf_to_png(compressed_pdf_path, os.path.join(path, f"{os.path.splitext(pdf_file)[0]}.png"), png_resolution)

    # 压缩 PNG 文件
    png_file_path = os.path.join(path, f"{os.path.splitext(pdf_file)[0]}.png")  # PNG 文件路径
    compress_png(png_file_path, png_quality)

def main():
    """主程序执行函数。"""
    # 删除所有 PNG 文件
    delete_png_files(path)
    
    # 获取所有 PDF 文件
    pdf_files = get_pdf_files(path)

    # 设置文件名前缀
    prefix = 'A'  # 文件名前缀

    # 重新编号和修改文件名
    renamed_files = rename_files(path, pdf_files, prefix)

    # 设置 PDF 和 PNG 的分辨率
    pdf_resolution = 150  # PDF 分辨率
    png_resolution = 100  # PNG 分辨率
    png_quality = '0-20'  # PNG 压缩质量范围

    # 使用 ThreadPoolExecutor 并行处理 PDF 文件
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(process_pdf, renamed_file, pdf_resolution, png_resolution, png_quality, prefix): renamed_file for renamed_file in renamed_files}
        for future in as_completed(futures):
            pdf_file = futures[future]
            try:
                future.result()  # 获取结果以处理可能发生的异常
                print(f'Processing complete: {pdf_file}')  # 打印处理完成的文件
            except Exception as e:
                print(f'Error processing {pdf_file}: {e}')  # 打印处理时的错误信息

    # 结束
    print('All processing complete.')  # 打印所有处理完成的信息

# 执行主函数
if __name__ == "__main__":
    main()

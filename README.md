# 机器学习算法实现项目

本项目实现并应用了多种机器学习算法,包括K-means聚类、主成分分析(PCA)、随机森林和感知机。项目主要针对手写数字识别和人体活动识别两个任务,同时也探索了机器学习中的基础概念如偏差-方差权衡。

## 项目结构

- `KMeans_PCA.py`: K-means聚类和PCA实现
- `Random_forests.py`: 随机森林实现和MNIST数据集分类
- `python_Bonus_BV.ipynb`: 感知机算法实现和偏差-方差分解分析
- `train.csv`: 人体活动识别数据集
- `traincsv.csv`: MNIST手写数字数据集
- `ML_Project3report.docx`: 项目报告文档

## 安装依赖

确保您的系统中已安装Python 3.x,然后运行以下命令安装所需依赖:

```bash
python -m pip install numpy pandas matplotlib scikit-learn scipy notebook
```

## 使用说明

1. K-means 和 PCA：脚本会覆盖当前目录下的 `train.csv`。请从仓库根目录把脚本和数据复制到临时目录运行，保留原始数据。
   ```bash
   scratch_dir="$(mktemp -d)"
   cp KMeans_PCA.py train.csv "$scratch_dir/"
   (cd "$scratch_dir" && python KMeans_PCA.py)
   ```

2. 随机森林分类:
   ```
   python Random_forests.py
   ```

3. 感知机和偏差-方差分析:
   在Jupyter Notebook中打开并运行`python_Bonus_BV.ipynb`

## 数据集

- MNIST数据集: 手写数字图像(traincsv.csv)
- 人体活动识别数据集: 包含各种传感器数据(train.csv)

## 主要功能

1. **K-means聚类和PCA**: 
   - 对人体活动数据进行聚类分析
   - 使用PCA进行数据可视化

2. **随机森林分类**:
   - 使用MNIST数据集训练随机森林模型
   - 进行手写数字识别
   - 模型评估和性能分析

3. **感知机算法和偏差-方差分析**:
   - 实现基本的感知机算法
   - 使用玩具数据集探索偏差-方差权衡

## 结果

- 课程记录中的随机森林准确率约为 88%。模型训练没有固定随机种子，重复运行可能得到不同结果。
- K-means聚类成功对人体活动数据进行了分组
- 通过感知机算法实现,深入理解了机器学习中的基本概念

## 贡献

欢迎对项目进行改进和扩展。如有任何问题或建议,请开issue或提交pull request。


# Machine Learning Algorithms Implementation Project

This project implements and applies various machine learning algorithms, including K-means clustering, Principal Component Analysis (PCA), Random Forest, and Perceptron. The project primarily focuses on handwritten digit recognition and human activity recognition tasks, while also exploring fundamental machine learning concepts such as the bias-variance tradeoff.

## Project Structure

- `KMeans_PCA.py`: Implementation of K-means clustering and PCA
- `Random_forests.py`: Random Forest implementation and MNIST dataset classification
- `python_Bonus_BV.ipynb`: Perceptron algorithm implementation and bias-variance decomposition analysis
- `train.csv`: Human Activity Recognition dataset
- `traincsv.csv`: MNIST handwritten digit dataset
- `ML_Project3report.docx`: Project report document

## Installation

Ensure you have Python 3.x installed on your system. Then run the following command to install the required dependencies:

```bash
python -m pip install numpy pandas matplotlib scikit-learn scipy notebook
```

## Usage

1. K-means and PCA: the script overwrites `train.csv` in its working directory. Run it on a temporary copy to preserve the original data. Start in the repository root.
   ```bash
   scratch_dir="$(mktemp -d)"
   cp KMeans_PCA.py train.csv "$scratch_dir/"
   (cd "$scratch_dir" && python KMeans_PCA.py)
   ```

2. Random Forest Classification:
   ```
   python Random_forests.py
   ```

3. Perceptron and Bias-Variance Analysis:
   Open and run `python_Bonus_BV.ipynb` in Jupyter Notebook

## Datasets

- MNIST Dataset: Handwritten digit images (traincsv.csv)
- Human Activity Recognition Dataset: Contains various sensor data (train.csv)

## Main Features

1. **K-means Clustering and PCA**: 
   - Perform cluster analysis on human activity data
   - Use PCA for data visualization

2. **Random Forest Classification**:
   - Train a Random Forest model using the MNIST dataset
   - Perform handwritten digit recognition
   - Model evaluation and performance analysis

3. **Perceptron Algorithm and Bias-Variance Analysis**:
   - Implement a basic Perceptron algorithm
   - Explore bias-variance tradeoff using toy datasets

## Results

- The coursework notes record about 88% accuracy for the random forest. The model has no fixed random seed, so reruns may differ.
- K-means clustering successfully grouped human activity data
- Gained deep understanding of basic machine learning concepts through Perceptron implementation

## Contributing

Improvements and extensions to the project are welcome. If you have any questions or suggestions, please open an issue or submit a pull request.

## License

The original README referenced an MIT license file. The current repository does not include that file.

## Project history

Former repository name: `ML_project3`. This repository preserves the original coursework and its development history.

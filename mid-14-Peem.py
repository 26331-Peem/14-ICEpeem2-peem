{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNIQ5N/KZUMwKwPua45s6+t",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/26331-Peem/14-ICEpeem2-peem/blob/main/mid_14_Peem_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Oh6v79jrrhnD",
        "outputId": "fc3355b2-5120-4231-f175-b946073ddc0e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "โปรเเกรมคำนวณกำลังไฟฟ้า\n",
            "ระบุกระเเสไฟฟ้า : 10\n",
            "ระบุค่าเเรงดันไฟฟ้า : 5\n",
            "ระบุค่าเเอมเเปร : 2\n",
            "\n",
            "ค่าเเรงดันไฟฟ้า :  10.0\n"
          ]
        }
      ],
      "source": [
        "print(\"โปรเเกรมคำนวณกำลังไฟฟ้า\")\n",
        "P = float(input(\"ระบุกระเเสไฟฟ้า : \"))\n",
        "V = float(input(\"ระบุค่าเเรงดันไฟฟ้า : \"))\n",
        "I = int(input(\"ระบุค่าเเอมเเปร : \"))\n",
        "\n",
        "formula = P = V * I\n",
        "print(\"\\nค่าเเรงดันไฟฟ้า : \",formula)"
      ]
    }
  ]
}

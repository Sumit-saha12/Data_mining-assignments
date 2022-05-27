{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "assignment2_datamining_26may.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyN4bMdpcnNKHO7UBm92XfRS"
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
      "source": [
        "# 1.PRINT YOU NAME 10 TIMES"
      ],
      "metadata": {
        "id": "Wu3v0TyE53sD"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cCDw66xo3zaC",
        "outputId": "d261494b-9548-410c-a19a-74d7e38175d6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "SUMIT SAHA\n",
            "SUMIT SAHA\n",
            "SUMIT SAHA\n",
            "SUMIT SAHA\n",
            "SUMIT SAHA\n",
            "SUMIT SAHA\n",
            "SUMIT SAHA\n",
            "SUMIT SAHA\n",
            "SUMIT SAHA\n",
            "SUMIT SAHA\n"
          ]
        }
      ],
      "source": [
        "for i in range(10):\n",
        "  print('SUMIT SAHA')"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 2. Write a program to take your monthly income as input \n",
        "If> 40,000/-\n",
        "Print  GOA TRIP,\n",
        "\n",
        "IF> 30,000 /- → SIKKIM \n",
        "IF >20,000 /- → DARJEELING\n",
        "IF > 10,000/- → DIGHA \n",
        "IF <  5000/- → MODI WANTS TO KNOW YOUR LOCATION"
      ],
      "metadata": {
        "id": "dMmQcVS-6l6h"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "monthly_salary=int(input('ENTER YOUR MONTHLY SALARY: '))\n",
        "\n",
        "if(monthly_salary>40000):\n",
        "  print('GOA TRIP')\n",
        "elif(30000<monthly_salary<=40000):\n",
        "  print('SIKKIM TRIP')\n",
        "elif(20000<monthly_salary<=30000):\n",
        "  print('DARJEELING TRIP')\n",
        "elif(10000<monthly_salary<=20000):\n",
        "  print('DIGHA TRIP')\n",
        "elif(monthly_salary<5000):\n",
        "  print('MODI WANIS TO KNOW YOUR LOCATION')"
      ],
      "metadata": {
        "id": "OMNyYPGb6QL_"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
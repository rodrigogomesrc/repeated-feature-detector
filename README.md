# repeated-feature-detector

Experimento usando deeplearning e template mathing para detectar se parte de uma imagem se repete. Ex: detectar imagens repetidas em uma colagem.


## Estrutura do projeto

O arquivo `dataset_generator.py` gera um dataset de imagens de colagem para testar a classificação e para treinar a rede neural (no caso da abordagem com deeplearning)

O arquivo `detector.py` contém a implementação utilizando template matching.

Já o arquivo `evaluate_detection.py` contém um script para avaliar a precisão do detector passando um dataset.


Os notebooks com as tentativas usando deeplearning estão na pasta `notebooks`.


## Como gerar o dataset

Execute o arquivo `dataset_generator.py` passando os seguintes parâmetros:

`<image_folder_path>` para o caminho da pasta onde estão as imagens que serão usadas para gerar o dataset

`<quantity>` para a quantidade de imagens que serão geradas

`<grid_size>` para o tamanho da grade de colagem. Ex: 3 para uma grade 3x3. (com 9 imagens)

`<resolution>` para a resolução das imagens geradas. Ex: uma colagem 3x3 com resolução 100 gerará imagens de 300x300

Exemplo de execução:

`python dataset-generator.py <images_folder_path> <quantity> <grid_size> <resolution>`

## Como executar o detector de padrões repetidos

Basta executar passando o caminho da imagem no lugar de `<image_path>`:

`Python3 detector.py <image_path>`

Ao executar o programa vai dizer se a imagem tem ou não padrões repetidos.

## Como calcular a acurácia do detector

Para calcular a acurácia o dataset utilizado devem contem as pastas "mathing" e "non-matching" conforme a estrutura
gerada no `dataset_generator.py`.

Tendo o dataset basta executar passando o caminho do dataset no lugar de `<folder_path>`:

`Python3 evaluate_detection.py <folder_path>`



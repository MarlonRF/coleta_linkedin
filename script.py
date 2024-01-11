from linkedin_api import Linkedin
import pandas as pd

# Substitua 'seu_email@dominio.com' e 'sua_senha_secreta' com suas credenciais reais
usuario = 'seu_email@dominio.com'
senha = 'sua_senha_secreta'

# Inicializa a API do LinkedIn com suas credenciais
api = Linkedin(usuario, senha)

# Substitua 'caminho/para/seu/arquivo.xlsx' pelo caminho real do seu arquivo Excel
caminho_total = 'caminho/para/seu/arquivo.xlsx'

# Lê o arquivo Excel
df = pd.read_excel(caminho_total)

# Obtém uma lista única de IDs do LinkedIn a partir da coluna 'LINKEDIN' do DataFrame
id_profiles = list(set(df['LINKEDIN']))

# Dicionário para armazenar dados dos perfis do LinkedIn
dados_profiles = {}

# Itera sobre os IDs dos perfis (limite de 500 requisições diárias a API)
for profile in id_profiles:
    try:
        # Tenta obter os dados do perfil usando a API do LinkedIn
        dados_profiles[profile] = api.get_profile(profile)
    except Exception as e:
        # Se houver um erro (perfil não encontrado, por exemplo), registra 'Não encontrado' e imprime o erro
        dados_profiles[profile] = 'Não encontrado'
        print(f"Erro ao obter dados para o perfil {profile}: {e}")

# Converte o dicionário em um DataFrame do pandas e transpõe (troca linhas por colunas)
df_resultado = pd.DataFrame(dados_profiles).T

# Fim do código

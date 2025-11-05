import pyodbc
import os

class conexao_msaccess:
    """
    Classe para conexão e operações básicas com um banco de dados Microsoft Access (.mdb ou .accdb).
    """

    def __init__(self, caminho_banco: str):
        """
        Inicializa a conexão com o banco de dados.
        :param caminho_banco: Caminho completo do arquivo .mdb ou .accdb
        """
        self.connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={caminho_banco}'

        try:
            self._con = pyodbc.connect(self.connection_string)
            print("✅ Conectado ao banco de dados com sucesso.")

        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == '01000':
                print("⚠️ Erro: incompatibilidade de arquitetura entre o driver e a aplicação.")
            else:
                print(f"❌ Erro ao conectar ao banco de dados: {ex}")
            raise ex


    # --------------------------------------------------------------------------
    # Métodos de manipulação de dados
    # --------------------------------------------------------------------------

    def insere(self, numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado, link):
        """Insere um novo registro na tabela projetos_de_lei."""
        try:
            cursor = self._con.cursor()
            cursor.execute(
                '''
                INSERT INTO projetos_de_lei
                (numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado, link)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                (numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado, link)
            )
            self._con.commit()
            print(f'(SQL) Registro {numero} inserido com sucesso.')

        except Exception as ex:
            print(f'❌ Erro ao inserir número {numero}: {ex}')


    def atualiza(self, numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado, link):
        """Atualiza um registro existente."""
        try:
            cursor = self._con.cursor()
            cursor.execute(
                '''
                UPDATE projetos_de_lei
                SET ementa = ?, data_publicacao = ?, autor = ?, comissoes = ?, tipo = ?, numero_formatado = ?, link = ?
                WHERE numero = ?
                ''',
                (ementa, data_publicacao, autor, comissoes, tipo, numero_formatado, link, numero)
            )
            self._con.commit()
            print(f'(SQL) Registro {numero} atualizado com sucesso.')

        except Exception as ex:
            print(f'❌ Erro ao atualizar número {numero}: {ex}')


    def seleciona(self, numero):
        """Seleciona um registro específico pelo número."""
        cursor = self._con.cursor()
        cursor.execute(
            '''
            SELECT numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado, link
            FROM projetos_de_lei WHERE numero = ?
            ''',
            (numero,)
        )
        return cursor.fetchone()


    def seleciona_formatado(self, numero_formatado):
        """Seleciona um registro específico pelo número."""
        cursor = self._con.cursor()
        cursor.execute(
            '''
            SELECT numero, ementa, data_publicacao, autor, comissoes, tipo, numero_formatado, link
            FROM projetos_de_lei WHERE numero_formatado = ?
            ''',
            (numero_formatado,)
        )
        return cursor.fetchone()


    def apaga(self, numero):
        """Apaga um registro específico."""
        cursor = self._con.cursor()
        cursor.execute('DELETE FROM projetos_de_lei WHERE numero = ?', (numero,))
        self._con.commit()
        print(f'(SQL) Registro {numero} excluído com sucesso.')


    def apaga_tudo(self):
        """Apaga todos os registros da tabela."""
        try:
            cursor = self._con.cursor()
            cursor.execute('DELETE FROM projetos_de_lei')
            self._con.commit()
            print('(SQL) Todos os registros foram apagados.')

        except Exception as ex:
            print(f'❌ Erro ao apagar todos os registros: {ex}')


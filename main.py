from neo4j import GraphDatabase

class Neo4jCRUD:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_node(self, label, properties):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_node_tx, label, properties)
            return result

    @staticmethod
    def _create_node_tx(tx, label, properties):
        query = f"CREATE (n:{label} {{ {', '.join(f'{k}: ${k}' for k in properties)} }}) RETURN n"
        result = tx.run(query, properties)
        return result.single()[0]

    def read_node(self, label, properties):
        with self.driver.session() as session:
            result = session.read_transaction(self._read_node_tx, label, properties)
            return result

    @staticmethod
    def _read_node_tx(tx, label, properties):
        query = f"MATCH (n:{label}) WHERE { ' AND '.join(f'n.{k} = ${k}' for k in properties) } RETURN n"
        result = tx.run(query, properties)
        return [record[0] for record in result]

    def update_node(self, label, match_properties, set_properties):
        with self.driver.session() as session:
            result = session.write_transaction(self._update_node_tx, label, match_properties, set_properties)
            return result

    @staticmethod
    def _update_node_tx(tx, label, match_properties, set_properties):
        query = f"MATCH (n:{label}) WHERE { ' AND '.join(f'n.{k} = ${k}' for k in match_properties) } SET { ', '.join(f'n.{k} = ${k}' for k in set_properties) } RETURN n"
        result = tx.run(query, {**match_properties, **set_properties})
        return [record[0] for record in result]

    def delete_node(self, label, properties):
        with self.driver.session() as session:
            result = session.write_transaction(self._delete_node_tx, label, properties)
            return result

    @staticmethod
    def _delete_node_tx(tx,label ,properties):
        query = f"MATCH (n:{label}) WHERE { ' AND '.join(f'n.{k} = ${k}' for k in properties) } DELETE n"
        tx.run(query ,properties)

# Example usage
if __name__ == "__main__":
    neo4j_crud = Neo4jCRUD("bolt://localhost:7687", "neo4j", "password")

    # Create node
    node = neo4j_crud.create_node("Person", {"name": "Alice", "age": 30})
    print(node)

    # Read node
    nodes = neo4j_crud.read_node("Person", {"name": "Alice"})
    print(nodes)

    # Update node
    updated_nodes = neo4j_crud.update_node("Person", {"name": "Alice"}, {"age": 31})
    print(updated_nodes)

    # Delete node
    neo4j_crud.delete_node("Person", {"name": "Alice"})

    neo4j_crud.close()
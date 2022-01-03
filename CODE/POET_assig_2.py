import hashlib
import json
import time
import random
class BlockChainTechnology:
    def __init__(self):
        self.current_trans = []
        self.chain = []
        self.nodes = set()
        self.new_block('1', 'Genisi_Node')
        self.default_nodes()

    def default_nodes(self):
        nodes = ["Miner_Ragav","Miner_Kesav"]
        for i in nodes:
            self.nodes.add(i)
            
    def Poet_Time_Stamp(self):
        temp_miner = self.nodes
        order = list()
        for i in temp_miner:
            x = random.randint(1,100)
            order.append(x)
        
        zipp = zip(order,temp_miner)
        sort = sorted(zipp,reverse=False)
        tuples = zip(*sort)
        order,temp_miner = [list(t) for t in tuples]
        print("New Miner Order==> ", temp_miner)
        return temp_miner
    def poet_mine(self):
        temp_trans = self.current_trans
        temp_miner = self.nodes
        order = list()
        temp_trans_remover = list()
        #print("temp_trans----->",temp_trans)
        temp_miner = self.Poet_Time_Stamp()
        count = 0
        for i in temp_trans:
            if(count < len(temp_miner)):
                temp_block = {
                'index': len(self.chain) + 1,
                'timestamp': time.time(),
                'transactions': i,
                'previous_hash': self.hash(self.chain[-1]),
                'node': temp_miner[count],
                }
                count += 1
                self.chain.append(temp_block)
                temp_trans_remover.append(i)
            else:
                break
        for i in temp_trans_remover:
            self.current_trans.remove(i)
        print("Mined")
            

    def register_node(self, address):
            parsed_url = address
            if True:
                self.nodes.add(parsed_url)
            else:
                raise ValueError('Invalid USER')
    def get_current(self):
        #print(self.current_trans)
        return self.current_trans
    def get_chain(self):
        print(self.chain)
        return len(self.chain)
    def new_block(self, prev_hash,node):
            block = {
                'index': len(self.chain) + 1,
                'timestamp': time.time(),
                'transactions': "Genesis",
                'previous_hash': prev_hash or self.hash(self.chain[-1]),
                'node': node,
            }
            if len(self.chain) == 0:
                self.chain.append(block)
            else:
                self.current_trans.append(block)

            #print("new_block ==>",block)
            return block
    def get_nodes(self):
        for i in self.nodes:
            print(i)
        return self.nodes
    def new_transaction(self,sender, amount, recipient):
            temp_transaction_block = {
                'sender': sender,
                'amount': amount,
                'recipient': recipient,
            }
            #print("Print BEFORe current ->",self.current_trans)
            self.current_trans.append(temp_transaction_block)
            
            #print("=================\nPrint current ->",self.current_trans)
            return len(self.current_trans)
    @staticmethod
    def hash(block):
            block_str = json.dumps(block, sort_keys= True).encode()
            return hashlib.sha256(block_str).hexdigest()

if __name__ == '__main__':
    blockchain = BlockChainTechnology()
    def register_nodes():
        values = input()
        nodes = values
        if nodes is None:
            return 'Error: Please supply a valid list of nodes', 400

        for node in nodes:
            blockchain.register_node(node)
        #blockchain.register_node(nodes)
        response = {
            'message': 'New nodes have been added',
            'total_nodes': list(blockchain.nodes),
        }
        print(response)
        return response, 201


    def new_transaction():
        values = {}
        print("Enter Sender ")
        values['sender'] = input()
        print("Enter Amount ")
        values['amount'] = input()
        print("Enter Recipient ") 
        values['recipient'] = input()

        index = blockchain.new_transaction(values['sender'], values['amount'], values['recipient'])

        response = {"NOTE ==> "f' Transaction Entered and will be added to Block'}
        #print(response)
        return response
    def Complete_chain_transation():
        response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
        }
        #print(response)
        return response
    def register_nodes():
        values = input()
        nodes = "Miner_"+values
        if nodes is None:
            return 'Error: Please supply a valid list of nodes', 400

        
        blockchain.register_node(nodes)
        #blockchain.register_node(nodes)
        response = {
            'message': 'New nodes have been added',
            'total_nodes': list(blockchain.nodes),
        }
        #print(response)
        return response




    def miner():
        #choose node
        temp_block = blockchain.poet_mine()
        return temp_block

        

    print("ctrl+c Exit Code")
    print("1__Register New Node")
    print("2__Verified Chain")
    print("3__New Transaction")
    print("4__Mine(POET)")
    print("5__List Current Transations")
    print("6__Node List")
    while(True):
        print("<==============================================>")
        i = int(input())
        if i > 6 or i < 1:
            print("Invalid Option")
        if i == 1:
            register_nodes()
            temp = blockchain.get_nodes()
            
        elif i == 2:
            temp = Complete_chain_transation()
            for i in temp:
                if i  == 'chain':
                    print("chain")
                    for k in temp['chain']:
                        for l in k:
                            print(l, k[l])
                        print("-------------------------------")
                else:
                    print(i,temp[i])        
                print("--------------------------------------------------")
        elif i == 3:
            print(new_transaction())

        elif i == 4:
            miner()
        elif i == 5:
            temp = blockchain.get_current()
            for i in temp:
                print(i)
                print("--------------------------------------------------")
        elif i == 6:
            blockchain.get_nodes()
    
    
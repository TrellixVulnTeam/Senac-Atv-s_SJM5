import { Component } from '@angular/core';
import { Storage } from '@ionic/storage-angular';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {
  constructor(private Storage: Storage) {}

  async ngOnInit() {  // cria o storage / banco de dados
    await this.Storage.create()
  }
}

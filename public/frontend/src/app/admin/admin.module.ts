import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CKEditorModule } from '@ckeditor/ckeditor5-angular';

import { AdminRoutingModule } from './admin-routing.module';
import { AdminRootComponent } from './admin-root/admin-root.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { HeaderComponent } from './common/header/header.component';
import { FooterComponent } from './common/footer/footer.component';
import { SidebarComponent } from './common/sidebar/sidebar.component';
import { QuestionDashboardComponent } from './question-bank/question-dashboard/question-dashboard.component';
import { AssessmentDashboardComponent } from './assessment/assessment-dashboard/assessment-dashboard.component';
import { CreateAssessmentComponent } from './assessment/create-assessment/create-assessment.component';
import { CoursesDashboardComponent } from './courses/courses-dashboard/courses-dashboard.component';

@NgModule({
  declarations: [AdminRootComponent,
    DashboardComponent,
    HeaderComponent,
    FooterComponent,
    SidebarComponent,
    QuestionDashboardComponent,
    AssessmentDashboardComponent,
    CreateAssessmentComponent,
    CoursesDashboardComponent],
  imports: [
    CommonModule,
    AdminRoutingModule,
    CKEditorModule
  ]
})
export class AdminModule { }
